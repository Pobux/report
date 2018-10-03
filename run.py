from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__,
           static_folder = "./dist/static",
           template_folder = "./dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/log')
def get():
    response = {
        "logs" : [
            "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Chosen certificate #1538574301 is valid from [2018-10-03] to [2018-10-04]",
            "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Server key fingerprint is DCA8:D3C8:9E5D:8A10:D925:CF1F:D8CE:8FE4:21FB:9574:6189:718D:A05F:7EBE:A7AB:DB6E"
        ]
    }

    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
