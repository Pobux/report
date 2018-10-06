from flask import Flask, render_template, jsonify, request

import json

app = Flask(__name__)


#Affiche la liste de tous les logs disponibles
@app.route('/log', methods=['GET'])
def get():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)


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
    app.run(port='5002')