import requests
import json

from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return 'Server Works!'


@app.route('/recaptcha', methods=['POST'])
def verify_recaptcha():
    token = request.form['token']

    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': '6Ldq6c4gAAAAADF7F-hAqzKbinGX_kynTo637KAW',
            'response': token,
        }
    )
    resp = json.loads(response.text)

    return {
        'google': resp,
        'token': token
    }
