from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import datetime
from app import sender

app = Flask(__name__,
           static_folder = "./dist/static",
           template_folder = "./dist")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/log')
def get():
    req = compose_request()
    print("Request :\n" + str(req))
    messenger = sender.Sender("localhost", req["queue"], 5672)

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
    return str(response)
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
        "args" : request.args
    }

    return req

def _get_queue_from_service(service):
    #TODO validate queue here with config file or direct look up
    return service.split("/")[0] + "_queue"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
