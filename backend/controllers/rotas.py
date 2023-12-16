from backend import *
from flask import Flask, render_template,redirect,request,flash,session,abort,url_for
import json
import requests as requests



@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/criar")
def criar():
    return "pagina de criar login"