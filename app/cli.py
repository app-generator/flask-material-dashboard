# -*- encoding: utf-8 -*-
"""
Flask Boilerplate
Author: AppSeed.us - App Generator 
"""

import      datetime,time,os,re
from sqlalchemy  import desc,or_

from flask_frozen import Freezer

from app         import app, lm, db, bc
from . common    import COMMON, DATATYPE
from . models    import User

def export_static():
    freezer = Freezer(app)
    freezer.freeze()

def create_user( email, name, username, password):

    # regex to check for e-mail syntax
    if not re.match("(^.+@{1}.+\.{1}.+)", str(email)):
        
        print("Invalid e-mail. Please try again.")
        return None
        #return "Invalid e-mail. Please try again."

    # hash the password here (bcrypt has salting included)
    pw_hash = bc.generate_password_hash(password)

    # if form is valid and all verification is complete
    # create User object and give the parameters in order
    user = User(username, pw_hash, name, email)

    user.save()

    print( "user created ok: " + str( user.id ) )
    return user 

# @ToDo - to be moved in a test file
def create_test_users():
    create_user( 'test@yahoo.com', 'Test User', 'test', 'pass1234') 
               