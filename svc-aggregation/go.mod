module github.com/ODIM-Project/ODIM/svc-aggregation

go 1.17

require (
	github.com/ODIM-Project/ODIM/lib-dmtf v0.0.0-20201201072448-9772421f1b55
	github.com/ODIM-Project/ODIM/lib-messagebus v0.0.0-20201201072448-9772421f1b55
	github.com/ODIM-Project/ODIM/lib-rest-client v0.0.0-20201201072448-9772421f1b55
	github.com/ODIM-Project/ODIM/lib-utilities v0.0.0-20201201072448-9772421f1b55
	github.com/satori/go.uuid v1.2.0
	github.com/sirupsen/logrus v1.6.0
	github.com/stretchr/testify v1.7.0
)

require (
	github.com/ODIM-Project/ODIM/lib-persistence-manager v0.0.0-20211220033333-4314870ed337 // indirect
	github.com/prometheus/common v0.32.1 // indirect
	github.com/prometheus/procfs v0.7.3 // indirect
	google.golang.org/grpc v1.41.0 // indirect
)

replace (
	github.com/ODIM-Project/ODIM/lib-dmtf => ../lib-dmtf
	github.com/ODIM-Project/ODIM/lib-messagebus => ../lib-messagebus
	github.com/ODIM-Project/ODIM/lib-persistence-manager => ../lib-persistence-manager
	github.com/ODIM-Project/ODIM/lib-rest-client => ../lib-rest-client
	github.com/ODIM-Project/ODIM/lib-utilities => ../lib-utilities
	google.golang.org/grpc v1.41.0 => google.golang.org/grpc v1.26.0
)
