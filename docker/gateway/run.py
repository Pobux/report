from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
from app import sender

app = Flask(__name__,
           static_folder = "./dist/static",
           template_folder = "./dist")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/log')
def get():
    #TODO do some validation, parsing, handling and whatnot
    messenger = sender.Sender("localhost", "log_queue", 5672)
    try:
        messenger.send("UN MESSAGE ENVOYÉ")
    except Exception as e:
        return "Failed\n"+str(e)

    print("waiting for service to answer")
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
    #TODO return 
    service = request.script_root
    return service

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
