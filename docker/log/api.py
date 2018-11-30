from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from log import log, log_factory, nice_json
import datetime
import re
import json

app = Flask(__name__)


# Affiche la liste de tous les logs disponibles
@app.route('/log', methods=['GET'])
def get():
    log_name = request.args['type']
    behavior = request.args['behavior']

    factory = log_factory.LogFactory()
    log = factory.create_log(log_name, behavior)
    logs = log.fetch_log()
    return nice_json(logs)

# Recuperer un log par sa date
@app.route('/log/date', methods=['GET'])
def api_id():
    log_name = request.args['type']
    behavior = request.args['behavior']

    if not is_log_type(log_name):
        return "Error: Incorrect log type, should be syslog or statlog"

    if not is_behavior(behavior):
        return "Error: Incorrect behavior, should be text or graph"

    factory = log_factory.LogFactory()
    log = factory.create_log(log_name, behavior)
    db = log.fetch_log()

    if 'date' in request.args:
        laDate = request.args['date']
        if not is_valid_date(laDate):
            return "Error: Invalid date format, should be YYYY-MM-DD"
    else:
        return "Error: No date field provided. Please specify an date."
    if laDate not in db:
        return "Error : date provide not found in the db."

    return nice_json(db[laDate])


def is_valid_date(une_date):
    try:
        datetime.datetime.strptime(une_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# def isValideDate2(une_date):
#
#    pattern = "^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
#    if not re.match(pattern, une_date):
#       return "Error: Incorrect data format, should be YYYY-MM-DD"

# def isValideDate3(une_date):
#
#    pattern = "^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
#    return re.match(pattern, une_date)



def is_behavior(behavior):
    liste = ["text", "graph"]
    return behavior in liste


def is_log_type(log_name):
    liste = ["syslog", "statlog"]
    return log_name in liste


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6001)
