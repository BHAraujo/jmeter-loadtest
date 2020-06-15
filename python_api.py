import json
from flask import Flask, request


app = Flask(__name__)


@app.route('/get/<string:nome>', methods=["GET"])
def get(nome):
    return "Hello, {}".format(nome), 200


@app.route('/post', methods=["POST"])
def post():
    if request.json is not None:
        return json.dumps(request.json), 201
    else:
        return "Campo nome não pode ser nulo", 400


if __name__ == "__main__":
    app.run(port=5000, debug=True)
