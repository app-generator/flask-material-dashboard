# -*- encoding: utf-8 -*-
"""
Material Dashboard - coded in Flask
Author: AppSeed.us - App Generator 
"""

# all the imports necessary
from flask import json, url_for, redirect, render_template, flash, g, session, jsonify, request, send_from_directory
from werkzeug.exceptions import HTTPException, NotFound, abort

import os

from app  import app

from flask       import url_for, redirect, render_template, flash, g, session, jsonify, request, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from app         import app, lm, db, bc
from . models    import User
from . common    import COMMON, STATUS
from . assets    import *
from . forms     import LoginForm, RegisterForm

import os, shutil, re, cgi
        
# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# authenticate user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))

# register user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    
    # define login form here
    form = RegisterForm(request.form)

    msg = None

    # custommize your pate title / description here
    page_title       = 'Register - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, registration page.'

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        name     = request.form.get('name'    , '', type=str) 
        email    = request.form.get('email'   , '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'
        
        else:                    
            pw_hash = bc.generate_password_hash(password)

            user = User(username, pw_hash, name, email)

            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'     

    # try to match the pages defined in -> /pages/
    return render_template( 'layouts/default.html',
                            title=page_title,
                            content=render_template( 'pages/register.html', form=form, msg=msg) )

# authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    # define login form here
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # custommize your page title / description here
    page_title = 'Login - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, login page.'

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        if user:
            
            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unkkown user"

    # try to match the pages defined in -> themes/light-bootstrap/pages/
    return render_template( 'layouts/default.html',
                            title=page_title,
                            content=render_template( 'pages/login.html', 
                                                     form=form,
                                                     msg=msg) )

# Used only for static export
@app.route('/icons.html')
def icons():

    # custommize your page title / description here
    page_title = 'Icons - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, the icons page.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/icons.html') )

# Used only for static export
@app.route('/notifications.html')
def notifications():

    # custommize your page title / description here
    page_title = 'Notifications - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, the notifications page.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/notifications.html') )

# Used only for static export
@app.route('/user.html')
def user():

    # custommize your page title / description here
    page_title = 'Profile - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, the profile page.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/user.html') )

# Used only for static export
@app.route('/tables.html')
def table():

    # custommize your page title / description here
    page_title = 'Tables - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, the tables page.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/tables.html') )

# Used only for static export
@app.route('/typography.html')
def typography():

    # custommize your page title / description here
    page_title = 'Typography - Flask Material Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Material Dashboard, the tables page.'

    # try to match the pages defined in -> pages/
    return render_template('layouts/default.html',
                            content=render_template( 'pages/typography.html') )

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

    content = None

    try:

        # try to match the pages defined in -> themes/light-bootstrap/pages/
        return render_template('layouts/default.html',
                                content=render_template( 'pages/'+path) )
    except:
        abort(404)

#@app.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'),
#                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#@app.route('/sitemap.xml')
#def sitemap():
#    return send_from_directory(os.path.join(app.root_path, 'static'),
#                               'sitemap.xml')

# ------------------------------------------------------

# error handling
# most common error codes have been added for now
# TO DO:
# they could use some styling so they don't look so ugly

def http_err(err_code):
	
    err_msg = 'Oups !! Some internal error ocurred. Thanks to contact support.'
	
    if 400 == err_code:
        err_msg = "It seems like you are not allowed to access this link."

    elif 404 == err_code:    
        err_msg  = "The URL you were looking for does not seem to exist."
        err_msg += "<br /> Define the new page in /pages"
    
    elif 500 == err_code:    
        err_msg = "Internal error. Contact the manager about this."

    else:
        err_msg = "Forbidden access."

    return err_msg
    
@app.errorhandler(401)
def e401(e):
    return http_err( 401) # "It seems like you are not allowed to access this link."

@app.errorhandler(404)
def e404(e):
    return http_err( 404) # "The URL you were looking for does not seem to exist.<br><br>
	                      # If you have typed the link manually, make sure you've spelled the link right."

@app.errorhandler(500)
def e500(e):
    return http_err( 500) # "Internal error. Contact the manager about this."

@app.errorhandler(403)
def e403(e):
    return http_err( 403 ) # "Forbidden access."

@app.errorhandler(410)
def e410(e):
    return http_err( 410) # "The content you were looking for has been deleted."

	