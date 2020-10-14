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
    decoded_token = auth.verify_id_token("eyJhbGciOiJSUzI1NiIsImtpZCI6IjIzNzA1ZmNmY2NjMTg4Njg2ZjhhZjkyYWJiZjAxYzRmMjZiZDVlODMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdGVzdC01YjA0ZSIsImF1ZCI6InRlc3QtNWIwNGUiLCJhdXRoX3RpbWUiOjE2MDI2MzIxNjAsInVzZXJfaWQiOiJ5S3lMbWt5SUttVFRyM1c3akpheTZ5Z1JVTHYyIiwic3ViIjoieUt5TG1reUlLbVRUcjNXN2pKYXk2eWdSVUx2MiIsImlhdCI6MTYwMjYzMjE3OSwiZXhwIjoxNjAyNjM1Nzc5LCJlbWFpbCI6InVzZXIzQHRlc3QuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInVzZXIzQHRlc3QuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.FAbIyH7KolZbQc_GgxbSJc--_LCwLC1IOgyPtqVNXlBMiVFR0YHMu96VCTdRLlLcaiTf6Lcj3fSFbeNnlEapHS8felMCIn0_sX4u6aRyoRYrta99nQtph1DeGXgVXSBtHJZth_tmeDQYYHRusltGxNujg46yJ-B5QQEJQzEPRoKUDzI9zduclj3AsL5u7a_0ZjFktZEenBHVKOxpT9L6wD8-DWzCO3d26jMCgliyXzDe_vxqetTS1ELOsCYCm753jVR8T8_uJXhXcg4cLPZaPWzEqVK_2S0ZIimBu4F2UCeZId83WDm1il78zAKE3yrP3oORyMH0v7MNCM4MaiRqCA")
    uid = decoded_token['uid']
    resultproxy = db.session.execute('SELECT * FROM users WHERE uid = :1', {'1': uid})
    response = format_resp(resultproxy)
    return jsonify(response)


app.run(debug=True)