from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import datetime
import json
from app import sender

app = Flask(__name__,
           static_folder = "./dist/static",
           template_folder = "./dist")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/log')
def get():
    req = compose_request()
    print("Request :\n" + str(req))
    messenger = sender.Sender("rabbit", req["queue"], 5672)

    try:
        print("Sending")
        messenger.send(req)
    except Exception as e:
        return "Failed\n"+str(e)

    try:
        response = messenger.manage_response()
    except Exception as e:
        #TODO add timeout exception
        return "Service timeout"

    #TODO check status_code
    print(response)
    print(type(response))
    print(type(response.decode('utf-8')))
    try:
        return jsonify(json.loads(response.decode('utf-8')))
    except:
        return response.decode("utf-8")
    # return jsonify(response.json())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Nothing here sorry, choose a path"

def compose_request():
    service = request.path #queue is derived from service path log -> log_queue
    method = request.url
    init = datetime.datetime.now().isoformat()
    args = request.args #?x=y part

    req = {
        "service" : service,
        "queue" : _get_queue_from_service(service),
        "init" : init,
        "method" : method,
        # "args" : request.args
        "args" : {
            "type" : "syslog",
            "behavior" : "text"
        }
    }

    return req

def _get_queue_from_service(service):
    #TODO validate queue here with config file or direct look up
    return service[1:].split("/")[0] + "_queue"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
