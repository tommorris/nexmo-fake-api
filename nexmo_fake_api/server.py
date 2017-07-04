from flask import Flask, jsonify, request
from utils import ErrorCollection, NO_API_KEY

app = Flask(__name__)

@app.route("/sms/json")
def sms_json():
    if 'api_key' not in request.form.keys():
        return jsonify(NO_API_KEY.format())

app.run()
