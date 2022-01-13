import logging
from config.config import PLUGIN_CONFIG
from config import constants
import json
from utilities.client import Client
from rest.resource_blocks import ResourceBlocks
from db.persistant import RedisClient
from http import HTTPStatus

class EventListener():

    def __init__(self):
        self.redis = RedisClient()
        self.client = Client()
        self.resource_blocks = ResourceBlocks()

    def listener(self, request_body):
        res = {}
        logging.info("in listener. config {}".format(PLUGIN_CONFIG))
        if PLUGIN_CONFIG["ManualEvent"]:
            # manual event listener
            self.manual_event_listener(request_body)
        else:
            self.event_listener(request_body)
        return res, HTTPStatus.ACCEPTED

    
    def event_listener(self, request_body):
        try:
            logging.debug("Composition Service Event Post Request body is {body}".format(body=request_body))
            if request_body.get("Events"):
                for value in request_body["Events"]:
                    origin_of_condition = value.get("OriginOfCondition")
                    if isinstance(origin_of_condition, dict):
                        origin_of_condition = origin_of_condition.get("@odata.id")
                    if not isinstance(origin_of_condition,str):
                        continue

                    origin_segments = origin_of_condition.split("/")
                    if len(origin_segments) > 1 and origin_segments[-1] and origin_segments[-2] == "Systems":
                        if value.get("EventType") and value["EventType"] in constants.EVENT_TYPES:
                            rb_keys = self.redis.keys("ResourceBlocks-ComputerSystem:*")
                            exist_cs_rb_key = None
                            for cs_rb_key in rb_keys:
                                if self.redis.get(cs_rb_key) == origin_of_condition:
                                    # exists = True
                                    exist_cs_rb_key = cs_rb_key
                                    break
                            
                            if exist_cs_rb_key is None:

                                # Resource Added
                                if value["EventType"] == "ResourceAdded":
                                    system_res = self.client.process_get_request(origin_of_condition)
                                    if system_res:
                                        # create resource block and set data into database
                                        self.resource_blocks.create_computer_sys_resource_block(system_res)
                            else:
                                # remaining event types
                                rb_key = exist_cs_rb_key.replace("-ComputerSystem", "")
                                resource_block_data = self.redis.get(rb_key)
                                if resource_block_data:
                                    resource_block_data = json.loads(resource_block_data)
                                
                                if value["EventType"] == "ResourceRemoved":
                                    
                                    if resource_block_data:
                                        # Update free pool and active pool
                                        if resource_block_data.get("Pool") == "Active":
                                            self.redis.srem("ActivePool", resource_block_data.get("@odata.id"))
                                        elif resource_block_data.get("Pool") == "Free":
                                            self.redis.srem("FreePool", resource_block_data.get("@odata.id"))


                                        if resource_block_data.get("Links"):
                                            # Delete Linked Composed Computer System
                                            if resource_block_data["Links"].get("ComputerSystems"):
                                                for system_uri in resource_block_data["Links"]["ComputerSystems"]:
                                                    if system_uri.get("@odata.id"):
                                                        self.redis.delete("ComputerSystem:{sys_uri}".format(sys_uri=system_uri["@odata.id"]))
                                            
                                            # Update Resource Block link in Resource Zone
                                            if resource_block_data["Links"].get("Zones"):
                                                for zone_uri in resource_block_data["Links"]["Zones"]:
                                                    if zone_uri.get("@odata.id"):
                                                        zone_key = "ResourceZones:{zuri}".format(zuri=zone_uri["@odata.id"])
                                                        zone_block_key = "{zone_block}:{zone_uri}".format(zone_block="ResourceZone-ResourceBlock", zone_uri=zone_uri["@odata.id"])
                                                        zone_block_link = self.redis.smembers(zone_block_key)
                                                        if len(zone_block_link) <= 1:
                                                            # if resource block linked zone is less than 1 then we can remove zone
                                                            self.redis.delete(zone_block_key, zone_key)
                                                        else:
                                                            self.redis.srem(zone_block_key, resource_block_data["@odata.id"])
                                                            # delete resource block link in ResourceZones data
                                                            zone_data = self.redis.get(zone_key)
                                                            if zone_data:
                                                                zone_data = json.loads(zone_data)
                                                                if zone_data.get("Links") and zone_data["Links"].get("ResourceBlocks"):
                                                                    for rb_uri in zone_data["Links"]["ResourceBlocks"]:
                                                                        if rb_uri.get("@odata.id") and rb_uri["@odata.id"] == resource_block_data["@odata.id"]:
                                                                            zone_data["Links"]["ResourceBlocks"].remove(rb_uri)
                                                                            self.redis.set(zone_key, str(json.dumps(zone_data)))
                                                                            break

                                    # delete resource block
                                    self.redis.delete(rb_key, exist_cs_rb_key)
                                    logging.info("successfully Removed the Resource Block for system {sys}".format(sys=origin_of_condition))

                                elif value["EventType"] in ["ResourceUpdated", "StatusChange", "Alert"]:
                                    system_res = self.client.process_get_request(origin_of_condition)
                                    
                                    
                                    change = False
                                    if system_res:
                                        if system_res.get("Status"):
                                            # check resource block status
                                            if resource_block_data and resource_block_data.get("Status"):
                                                if resource_block_data["Status"].get("Health") != system_res["Status"].get("Health"):
                                                    change = True
                                                    resource_block_data["Status"]["Health"] = system_res["Status"]["Health"]

                                                if resource_block_data["Status"].get("State") != system_res["Status"].get("State"):
                                                    change = True
                                                    resource_block_data["Status"]["State"] = system_res["Status"]["State"]
                                                if change:
                                                    self.redis.set(rb_key, str(json.dumps(resource_block_data)))

                                            # check composed system status
                                            if resource_block_data.get("Links"):
                                            # Delete Linked Composed Computer System
                                                if resource_block_data["Links"].get("ComputerSystems"):
                                                    for system_uri in resource_block_data["Links"]["ComputerSystems"]:
                                                        if system_uri.get("@odata.id"):
                                                            composed_sys_data = self.redis.get("ComputerSystem:{sys_uri}".format(sys_uri=system_uri["@odata.id"]))
                                                            if composed_sys_data:
                                                                composed_sys_data = json.loads(composed_sys_data)
                                                                if composed_sys_data.get("Status"):
                                                                    if composed_sys_data["Status"].get("Health") != system_res["Status"].get("Health"):
                                                                        change = True
                                                                        composed_sys_data["Status"]["Health"] = system_res["Status"]["Health"]

                                                                    if composed_sys_data["Status"].get("State") != system_res["Status"].get("State"):
                                                                        change = True
                                                                        composed_sys_data["Status"]["State"] = system_res["Status"]["State"]
                                                                    if change:
                                                                        self.redis.set("ComputerSystem:{sys_uri}".format(sys_uri=system_uri["@odata.id"]), str(json.dumps(composed_sys_data)))


                                                # check resource zone status with resource block
                                                if resource_block_data["Links"].get("Zones"):
                                                    for zone_uri in resource_block_data["Links"]["Zones"]:
                                                        if zone_uri.get("@odata.id"):
                                                            zone_key = "ResourceZones:{zuri}".format(zuri=zone_uri["@odata.id"])
                                                            zone_data = self.redis.get(zone_key)
                                                            if zone_data:
                                                                zone_data = json.loads(zone_data)
                                                                if zone_data.get("Links") and zone_data["Links"].get("ResourceBlocks"):
                                                                    rb_healths = []
                                                                    rb_states = []

                                                                    for rb_uri in zone_data["Links"]["ResourceBlocks"]:
                                                                        if rb_uri.get("@odata.id"):
                                                                            if rb_uri["@odata.id"] == resource_block_data["@odata.id"]:
                                                                                rb_healths.append(resource_block_data["Status"]["Health"])
                                                                                rb_states.append(resource_block_data["Status"]["State"])
                                                                            else:
                                                                                rb_data = self.redis.get("ResourceBlocks:{rburi}".format(rburi=rb_uri["@odata.id"]))
                                                                                if rb_data:
                                                                                    rb_data = json.loads(rb_data)
                                                                                    rb_healths.append(rb_data["Status"]["Health"])
                                                                                    rb_states.append(resource_block_data["Status"]["State"])
                                                                    accepted_health = ["OK", "Warning", "Critical"]
                                                                    for health in accepted_health:
                                                                        if health in rb_healths:
                                                                            zone_data["Status"]["Health"] = health
                                                                            break
                                                                    if "Enabled" in rb_states:
                                                                        zone_data["Status"]["State"] = "Enabled"
                                                                    else:
                                                                        zone_data["Status"]["State"] = "Disabled"



            logging.info(
                "succesfully finished Composition Service Event Post Operation")
        except Exception as err:
            logging.error("Unable to listen Composition service Events. Error: {e}".format(e=err))
        


    def manual_event_listener(self, request_body):
        pass
