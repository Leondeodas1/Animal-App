from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'animal_farm'


class Dinosaurs:
    def __init__( self , data ):
        self.id = data['id']
        self.dino_name = data['dino_name']
        self.length = data['length']
        self.when_it_lived = data['when_it_lived']
        self.Description = data['Description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 

    @staticmethod
    def validate_create(request):
        is_valid = True
        if len(request['dino_name']) < 1:
            flash("please Enter A  Dinosaut name", 'regError')
            is_valid = False
        elif len(request['dino_name']) < 3:
            flash("First Name must be longer than two characters",'regError')
            is_valid = False 
        if len(request['length']) < 0:
            flash("please enter a last_name",'regError')
            is_valid = False
        elif len(request['length']) < 1:
            flash("length must be longer than two characters", 'regError')
            is_valid = False 
        if len(request['when_it_lived']) < 1:
            flash("please enter a last_name",'regError')
            is_valid = False
        elif len(request['when_it_lived']) < 9:
            flash("Last Name must be longer than nine characters",'regError')
            is_valid = False 
        if len(request['Description']) < 1:
            flash("please confirm password",'regError')
            is_valid = False
        elif len(request['Description']) < 3:
            flash("First Name must be longer than two characters",'regError')
            is_valid = False 
        return is_valid 


    @classmethod
    def save_dino(cls, data ):
        query = "INSERT INTO dinosaurs ( dino_name , length , when_it_lived ,Description, created_at, updated_at ) VALUES ( %(dino_name)s , %(length)s , %(when_it_lived)s ,%(Description)s, NOW() , NOW());"
                
        return connectToMySQL(mydb).query_db( query, data )
 
    @classmethod
    def getalldino(cls):
        query = "select * from dinosaurs"
        results = connectToMySQL(mydb).query_db(query)
        print (results)
        return results
    
    @classmethod
    def search(cls):
        query = "select * from dinosaurs where dino_name = %(searched_animals)s";
        results = connectToMySQL(mydb).query_db(query)
        print(results)
        return results