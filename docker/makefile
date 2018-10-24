#Manager
MANAGER=manager
MANAGER_IP=$(shell docker-machine ip manager)

#API
API=gateway

#Microservices
##Logging services
LOGA=logA

LOGB=logB

TOKEN=$1

all:
	#"Choose an option, run with sudo."

manager:
	docker-machine ssh $(MANAGER) "docker swarm init --advertise-addr $(MANAGER_IP)"

workers:
	docker-machine ssh $(API) "docker swarm join --token $(TOKEN) $(MANAGER_IP):2377"
	docker-machine ssh $(LOGA) "docker swarm join --token $(TOKEN) $(MANAGER_IP):2377"
	docker-machine ssh $(LOGB) "docker swarm join --token $(TOKEN) $(MANAGER_IP):2377"
	
dockermachine:
	#"Creating Manager"
	docker-machine create $(MANAGER)
	#"Creating Gateway"
	docker-machine create $(API)
	#"Creating Microservices Logs"
	docker-machine create $(LOGA)
	docker-machine create $(LOGB)
	#"..."
	#"..."
	docker-machine ls

rmdockermachine:
	docker-machine rm $(MANAGER)
	docker-machine rm $(API)
	docker-machine rm $(LOGA)
	docker-machine rm $(LOGB)
