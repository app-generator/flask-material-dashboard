# -*- encoding: utf-8 -*-
"""
Flask Boilerplate
Author: AppSeed.us - App Generator 
"""

import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Only cfg is here .. 
class AppConfig(object):

	THEME = 'phantom' # 'argon-dashboard'

	STATIC  	 = 'static'
	DATE_FORMAT  = '%Y-%m-%d'
	SECRET_KEY   = "SuperSecret_77554##@3" # save yours here

class Config(AppConfig):
	"""
	Configuration base, for all environments.
	"""
	DEBUG                 			= False
	TESTING               			= False
	BOOTSTRAP_FONTAWESOME 			= True
	CSRF_ENABLED          			= True

	SQLALCHEMY_TRACK_MODIFICATIONS 	= False

class ProductionConfig(Config):

	APP = 'PATH_FOR_PRODUCTION'
	APP_IMG_FOLDER = os.path.join( APP, 'static', 'images' )

	# RECAPTCHA keys (production)
	RECAPTCHA_PUBLIC_KEY  = "1234_abcd"
	RECAPTCHA_PRIVATE_KEY = "1234_xyzw"

	#SQLALCHEMY_DATABASE_URI = "mysql+pymysql://db_user:db_pass@localhost/db_name"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

	SERVER_NAME   = 'www.yourdomain.us'
	DEBUG         = False
	TESTING       = False

class DevelopmentConfig(Config):

	APP = 'app'
	APP_IMG_FOLDER = os.path.join( APP, 'static', 'images' )

	# keys for dev [ http://localhost ]
	RECAPTCHA_PUBLIC_KEY  = "1234_abcd"
	RECAPTCHA_PRIVATE_KEY = "1234_xyzw"

	#SQLALCHEMY_DATABASE_URI = "mysql+pymysql://MYSQL_USER:MYSQL_PASS@localhost/MYSQL_DATABASE"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

	SERVER_NAME   = 'localhost:5000'
	DEBUG	= False
	TESTING	= False
	FORCE_HTTPS = False


