import firebase_admin
import os
from dotenv import load_dotenv
from firebase_admin import auth, credentials
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from helpers import format_resp

load_dotenv()

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)

app = Flask(__name__)
CORS(app)
Session(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
db = SQLAlchemy(app)

@app.route('/')
def running():
    return jsonify("Flask Server Running")

@app.route('/test')
def test():
    decoded_token = auth.verify_id_token("eyJhbGciOiJSUzI1NiIsImtpZCI6IjIzNzA1ZmNmY2NjMTg4Njg2ZjhhZjkyYWJiZjAxYzRmMjZiZDVlODMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdGVzdC01YjA0ZSIsImF1ZCI6InRlc3QtNWIwNGUiLCJhdXRoX3RpbWUiOjE2MDI2ODA3MDAsInVzZXJfaWQiOiJENFBlNFh3SHAwWm1Tc283ZWs0amN1NWZuWUgyIiwic3ViIjoiRDRQZTRYd0hwMFptU3NvN2VrNGpjdTVmbllIMiIsImlhdCI6MTYwMjY4MDcwOCwiZXhwIjoxNjAyNjg0MzA4LCJlbWFpbCI6InVzZXIxQHRlc3QuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInVzZXIxQHRlc3QuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.nKnsEa8QEOGq2vlkMPa3k-NRWUeUpoBl4gqXYDKNOrId8EDqwU_a-mvOwIxoR-wVmGyEeUCpbx7TQEm8jzJxERNiOPiyCeEvcrcdR_ofeSQffj2DQVl8okLkVf5ff9yJ8OrRTszSKRl3CLeoSR9gBBfIhWoZiJPXKga1W-GorbTyv7qFMjDzgCejVbge7z0axaD9teNtOMd1aq-bGIYO7njJCHVfUd0xiCj9mYwEo5ckUtlOFti5L-AcRxAgIuIByUFiPtQuF24TGralRRlIsgAylfqVrDu-hAB2aBWKtL7IV7Et4Wjgfc6CDyxDwYuR7RLhDKHuCh3wO-EGBmKBYQ")
    uid = decoded_token['uid']
    resultproxy = db.session.execute('SELECT username FROM users WHERE uid = :1', {'1': uid})
    response = format_resp(resultproxy)
    return jsonify(response[0])


app.run(debug=True)