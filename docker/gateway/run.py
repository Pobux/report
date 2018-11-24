from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
from app import rabbit

app = Flask(__name__,
           static_folder = "./dist/static",
           template_folder = "./dist")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/log')
def get():
    #TODO do some validation, parsing, handling and whatnot
    req = build_request()
    print("service")
    print(req)
    send(req)
    response = receive(req)
    response = requests.get("http://logservice:6001/log")
    #TODO check status_code
    return jsonify(response.json())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Nothing here sorry, choose a path"

def compose_request():
    #TODO return 
    service = request.script_root
    return service

def send(resource):
    messenger = rabbit.Rabbit()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
