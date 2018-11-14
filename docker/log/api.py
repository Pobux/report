from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from log import log

import json

app = Flask(__name__)

#Affiche la liste de tous les logs disponibles
@app.route('/log', methods=['GET'])
def get():
    #TODO call database
    response = {
        "logs" : [
            "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Chosen certificate #1534574301 is valid from [2018-10-03] to [2018-10-04]",
            "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Server key fingerprint is DCA8:D3C8:9E5D:8A10:D925:CF1F:D8CE:8FE4:21FB:9574:6189:718D:A05F:7EBE:A7AB:DX6E",
            "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Chosen certificate #1534574301 is invalid"
        ]
    }
    return jsonify(response)

#Recuperer un log par sa date
@app.route('/log/date', methods=['GET'])
def api_id():
    with open('data.json') as f:
        logs = json.load(f)

    if 'date' in request.args:
        laDate = request.args['date']
    else:
        return "Error: No date field provided. Please specify an date."

    results = []

    for log in logs:
        if log['date'] == laDate:
            results.append(log)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6001)
