from flask import Flask, render_template,redirect,request,flash
import pyrebase
app= Flask(__name__, template_folder="../frontend/App/templates")
app.config['SECRET_KEY']="IMAGSEGURA"
app.secret_key='IMAGSEGURA'
config={
  "apiKey": "AIzaSyAZ2b7BN9YrS9JrL-PVYkoV6H0Es2VPBns",
  "authDomain": "imag-chat.firebaseapp.com",
  "projectId": "imag-chat",
  "storageBucket": "imag-chat.appspot.com",
  "messagingSenderId": "659173782471",
  "appId": "1:659173782471:web:e9bc2dcdbbeab0130c1fe2",
  "measurementId": "G-408TXBM341",
  "databaseURL":"https://imag-chat-default-rtdb.firebaseio.com/"
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
from backend.controllers import rotas