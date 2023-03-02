from flask_app import app
from flask import render_template,request, redirect,session
from flask_app.models import user
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/home') 
def home():
    return render_template('home.html') 

@app.route('/backtohome')
def backtohome():
    return redirect('/home')