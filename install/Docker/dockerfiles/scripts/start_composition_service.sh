#!/bin/bash
#(C) Copyright [2022] American Megatrends International LLC
#
#Licensed under the Apache License, Version 2.0 (the "License"); you may
#not use this file except in compliance with the License. You may obtain
#a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#License for the specific language governing permissions and limitations
# under the License.

declare PID=0
declare OWN_PID=$$

sigterm_handler()
{
        if [[ $PID -ne 0 ]]; then
                sleep 1
                kill -9 $PID
                wait "$PID" 2>/dev/null
        fi
        exit 0
}

# create a signal trap
create_signal_trap()
{
        trap 'echo "[$(date)] -- INFO  -- SIGTERM received for composition service, initiating shut down"; sigterm_handler' SIGTERM
}

# keep the script running till SIGTERM is received
run_forever()
{
        wait
}

start_composition_service()
{
        registry_address="etcd:2379"
        export CONFIG_FILE_PATH=/etc/composition_service_config/config.json

        nohup /bin/svc-composition-service --registry=etcd --registry_address=${registry_address} --server_address=composition-service:45112 >> /var/log/odimra_logs/composition_service.log 2>&1 &
	PID=$!
	sleep 3

	nohup /bin/add-hosts -file /tmp/host.append >> /var/log/odimra_logs/composition-service-add-hosts.log 2>&1 &
}


##############################################
###############  MAIN  #######################
##############################################

start_composition_service

create_signal_trap

run_forever

exit 0
