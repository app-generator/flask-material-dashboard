# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
import pandas as pd
import os

db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

        file_path = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(file_path, 'pregnancy.csv')
        pregnancy = pd.read_csv(file, encoding="utf8")
        pregnancy.to_sql("Pregnancy", con= db.create_engine('sqlite:///db.sqlite3', {}), if_exists = 'replace', index=False)

        file = os.path.join(file_path, 'tips.csv')
        tips = pd.read_csv(file, encoding="utf8")
        tips.to_sql("Tips", con=db.create_engine('sqlite:///db.sqlite3', {}), if_exists='replace', index=False)

        file = os.path.join(file_path, 'prenatal.csv')
        prenatal = pd.read_csv(file, encoding="utf8")
        prenatal.to_sql("Prenatal", con=db.create_engine('sqlite:///db.sqlite3', {}), if_exists='replace', index=False)

        file = os.path.join(file_path, 'support.csv')
        support = pd.read_csv(file, encoding="utf8")
        support.to_sql("Support", con=db.create_engine('sqlite:///db.sqlite3', {}), if_exists='replace', index=False)



    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app



