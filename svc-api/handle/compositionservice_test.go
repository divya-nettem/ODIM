//(C) Copyright [2020] Hewlett Packard Enterprise Development LP
//
//Licensed under the Apache License, Version 2.0 (the "License"); you may
//not use this file except in compliance with the License. You may obtain
//a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
//WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
//License for the specific language governing permissions and limitations
// under the License.
package handle

import (
	"errors"
	"net/http"
	"testing"

	compositionserviceproto "github.com/ODIM-Project/ODIM/lib-utilities/proto/compositionservice"
	iris "github.com/kataras/iris/v12"
	"github.com/kataras/iris/v12/httptest"
)

func mockGetCompositionResource(req compositionserviceproto.CompositionResourceRequest) (*compositionserviceproto.CompositionServiceResponse, error) {
	var response = &compositionserviceproto.CompositionServiceResponse{}
	if req.SessionToken == "ValidToken" {
		response = &compositionserviceproto.CompositionServiceResponse{
			StatusCode:    200,
			StatusMessage: "Success",
			Body:          []byte(`{"Response":"Success"}`),
		}
	} else if req.SessionToken == "" {
		response = &compositionserviceproto.CompositionServiceResponse{
			StatusCode:    401,
			StatusMessage: "Unauthorized", Body: []byte(`{"Response":"Unauthorized"}`),
		}
	} else if req.SessionToken == "TokenRPC" {
		return nil, errors.New("RPC Error")
	}
	return response, nil
}

func mockDeleteDeleteCompositionResource(req compositionserviceproto.CompositionResourceRequest) (*compositionserviceproto.CompositionServiceResponse, error) {
	var response = &compositionserviceproto.CompositionServiceResponse{}
	if req.SessionToken == "ValidToken" {
		response = &compositionserviceproto.CompositionServiceResponse{
			StatusCode:    200,
			StatusMessage: "Success",
			Body:          []byte(`{"Response":"Success"}`),
		}
	} else if req.SessionToken == "" {
		response = &compositionserviceproto.CompositionServiceResponse{
			StatusCode:    401,
			StatusMessage: "Unauthorized", Body: []byte(`{"Response":"Unauthorized"}`),
		}
	} else if req.SessionToken == "TokenRPC" {
		return nil, errors.New("RPC Error")
	}
	return response, nil
}

func TestGetCompositionResource(t *testing.T) {
	var compositionservice CompositionServiceRPCs
	compositionservice.GetCompositionServiceRPC = mockGetCompositionResource
	mockApp := iris.New()
	redfishRoutes := mockApp.Party("/redfish/v1/CompositionService")
	redfishRoutes.Get("/", compositionservice.GetCompositionService)
	
	test := httptest.New(t, mockApp)
	test.GET(
		"/redfish/v1/CompositionService/",
	).WithHeader("X-Auth-Token", "ValidToken").Expect().Status(http.StatusOK)
	test.GET(
		"/redfish/v1/CompositionService/",
	).WithHeader("X-Auth-Token", "").Expect().Status(http.StatusUnauthorized).Headers().Equal(header)
	test.GET(
		"/redfish/v1/CompositionService/",
	).WithHeader("X-Auth-Token", "TokenRPC").Expect().Status(http.StatusInternalServerError).Headers().Equal(header)
}

func TestDeleteFabricResource(t *testing.T) {
	var fabrics FabricRPCs
	fabrics.DeleteFabricResourceRPC = mockDeleteFabricResource
	mockApp := iris.New()
	redfishRoutes := mockApp.Party("/redfish/v1/Fabrics")
	redfishRoutes.Get("/", fabrics.DeleteFabricResource)
	test := httptest.New(t, mockApp)
	test.GET(
		"/redfish/v1/Fabrics/",
	).WithHeader("X-Auth-Token", "ValidToken").Expect().Status(http.StatusOK).Headers().Equal(header)
	test.GET(
		"/redfish/v1/Fabrics/",
	).WithHeader("X-Auth-Token", "").Expect().Status(http.StatusUnauthorized)
	test.GET(
		"/redfish/v1/Fabrics/",
	).WithHeader("X-Auth-Token", "TokenRPC").Expect().Status(http.StatusInternalServerError)
}


