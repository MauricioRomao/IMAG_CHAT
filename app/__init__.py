from flask import Flask, render_template,redirect,request,flash


app= Flask(__name__)
app.config['SECRET_KEY']="IMAGSEGURA"
from app.controllers import rotas