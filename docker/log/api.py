from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from log import log, log_factory, nice_json
import json

app = Flask(__name__)

#Affiche la liste de tous les logs disponibles
@app.route('/log', methods=['GET'])
def get():

    log_name = request.args['type']
    behavior = request.args['behavior']

    factory = log_factory.LogFactory()
    log = factory.create_log(log_name, behavior)
    logs = log.fetch_log()
    return nice_json(logs)


#Recuperer un log par sa date
@app.route('/log/date', methods=['GET'])
def api_id():
    log_name = request.args['type']
    behavior = request.args['behavior']

    factory = log_factory.LogFactory()
    log = factory.create_log(log_name, behavior)
    db = log.fetch_log()

    if 'date' in request.args:
        laDate = request.args['date']
    else:
        return "Error: No date field provided. Please specify an date."

    if laDate not in db:
        return "Error : date provide not found in the db."

    return nice_json(db[laDate])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6001)
