#Linux make file, don't use this on windows. Maybe it works on a Mac.
VIRTUALENV = $(shell which virtualenv)


start:
	#Make sure you are under virtualenv
	. backend/env/bin/activate
	FLASK_APP=run.py FLASK_DEBUG=1 flask run

frontend:
	npm install -g vue-cli
	mkdir -p vue
	cd vue
	vue init webpack frontend
	cd frontend
	npm install

backend:
	mkdir -p backend
	cd backend
	apt install virtualenv -y
	virtualenv -p python3 venv

npm:
	apt update
	apt install nodejs -y
	nodejs --version
	apt install npm -y
	npm --version
