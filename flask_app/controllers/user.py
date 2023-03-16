from flask_app import app
from flask import render_template,request, redirect,session
from flask_app.models import user
from flask_app.models import dinosuar_models
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)
dateFormat = "%m/%d/%Y %I:%M %p"
from flask import jsonify


@app.route('/home') 
def home():
    return render_template('home.html') 

@app.route('/backtohome')
def backtohome():
    return redirect('/home')

@app.route('/get_data') 
def adddata():
    return render_template('dinosaur.html', dinopower = dinosuar_models.Dinosaurs.getalldino())

@app.route('/add_dinosaur', methods = ['POST'])
def create_dina():
    if 'users_id' not in session:
        return redirect('/home')
    if not dinosuar_models.Dinosaurs.validate_create(request.form):
        return redirect('/get_data')
    dinosuar_models.Dinosaurs.save_dino(request.form)
    print(request.form)
    return redirect('/home')

@app.route('/get_search', methods = ['GET'])
def new_templates():
    return render_template("animal.html")

@app.route('/nothgin', methods = ['GET'])
def find_dino():
    data = {
        "searched_animals" : request.form['search_animal']
    }
    print(data)
    dinosuar_models.Dinosaurs.search(data)
    return redirect('/home')