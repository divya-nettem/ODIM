module github.com/ODIM-Project/ODIM/plugin-redfish

go 1.17

require (
	github.com/ODIM-Project/ODIM/lib-dmtf v0.0.0-20210201172557-4fa2adafe1e3
	github.com/ODIM-Project/ODIM/lib-messagebus v0.0.0-20201201072448-9772421f1b55
	github.com/ODIM-Project/ODIM/lib-utilities v0.0.0-20201201072448-9772421f1b55
	github.com/fsnotify/fsnotify v1.4.9
	github.com/gofrs/uuid v3.2.0+incompatible
	github.com/kataras/iris/v12 v12.1.9-0.20200616210209-a85c83b70ad0
	github.com/satori/go.uuid v1.2.0
	github.com/sirupsen/logrus v1.4.2
	golang.org/x/crypto v0.0.0-20210711020723-a769d52b0f97
)

require (
	github.com/mattn/go-colorable v0.1.11 // indirect
	github.com/yudai/pp v2.0.1+incompatible // indirect
)

replace (
	github.com/ODIM-Project/ODIM/lib-dmtf => ../lib-dmtf
	github.com/ODIM-Project/ODIM/lib-messagebus => ../lib-messagebus
	github.com/ODIM-Project/ODIM/lib-persistence-manager => ../lib-persistence-manager
	github.com/ODIM-Project/ODIM/lib-rest-client => ../lib-rest-client
	github.com/ODIM-Project/ODIM/lib-utilities => ../lib-utilities
)
