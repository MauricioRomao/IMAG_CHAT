from flask import Flask, render_template,redirect,request,flash
app= Flask(__name__, template_folder="../frontend/App/templates")
app.config['SECRET_KEY']="IMAGSEGURA"
from backend.controllers import rotas