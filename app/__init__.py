# -*- encoding: utf-8 -*-
"""
Flask Boilerplate
Author: AppSeed.us - App Generator 
"""

from flask            import Flask
from flask_bootstrap  import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt
from flask_mail       import Mail


# load RES
from . import assets  

app = Flask(__name__, static_url_path='/static')

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('app.configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')

# Expose globals to Jinja2 templates
app.add_template_global(assets     , 'assets')
app.add_template_global(app.config , 'cfg'   )

db   = SQLAlchemy  (app) #flask-sqlalchemy
lm   = LoginManager(   ) #flask-loginmanager
bc   = Bcrypt      (app) #flask-bcrypt

lm.init_app(app) # init the login manager

from app import views, models
