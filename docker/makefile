root=$(shell pwd)

gateway:
	cd $(root)/gateway
	docker build -t gateway:latest gateway 
	docker run -d -p 5000:8080 gateway

.PHONY: gateway
