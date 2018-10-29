from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__,
           static_folder = "./dist/static",
           template_folder = "./dist")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/log')
def get():
    #TODO do some validation, parsing, handling and whatnot
    response = requests.get("http://logservice:6001/log")
    #TODO check status_code
    return jsonify(response.json())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Nothing here sorry, choose a path"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
