module github.com/ODIM-Project/ODIM/svc-api

go 1.17

require (
	github.com/ODIM-Project/ODIM/lib-utilities v0.0.0-20210622112605-b6361e8ba368
	github.com/kataras/iris/v12 v12.1.9-0.20200616210209-a85c83b70ad0
	github.com/sirupsen/logrus v1.6.0
)

require (
	github.com/ODIM-Project/ODIM/lib-dmtf v0.0.0-20210901061202-f84c396a018e
	github.com/coreos/go-systemd v0.0.0-20191104093116-d3cd4ed1dbcf // indirect
	github.com/coreos/pkg v0.0.0-20180928190104-399ea9e2e55f // indirect
	github.com/mattn/go-colorable v0.1.11 // indirect
	github.com/niemeyer/pretty v0.0.0-20200227124842-a10e7caefd8e // indirect
	github.com/prometheus/common v0.32.1 // indirect
	github.com/prometheus/procfs v0.7.3 // indirect
	github.com/yudai/pp v2.0.1+incompatible // indirect
	google.golang.org/grpc v1.41.0 // indirect
	gopkg.in/check.v1 v1.0.0-20200902074654-038fdea0a05b // indirect
)

replace (
	github.com/ODIM-Project/ODIM/lib-dmtf => ../lib-dmtf
	github.com/ODIM-Project/ODIM/lib-messagebus => ../lib-messagebus
	github.com/ODIM-Project/ODIM/lib-persistence-manager => ../lib-persistence-manager
	github.com/ODIM-Project/ODIM/lib-rest-client => ../lib-rest-client
	github.com/ODIM-Project/ODIM/lib-utilities => ../lib-utilities
	google.golang.org/grpc v1.41.0 => google.golang.org/grpc v1.26.0
)
