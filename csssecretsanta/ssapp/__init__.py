#this file creates the webapp and configures settings
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap
from flask import Flask
from flask_mail import Mail
bootstrap = Bootstrap()
#creates the webapp
app = Flask(__name__)
app.secret_key='sidskey'

#gets all specified configurations from 'config.py'
app.config.from_pyfile('settings.py')
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280

#create database ORM mapping
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#email configurations
app.config.update(DEBUG=True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'secsanta9@gmail.com',
    MAIL_PASSWORD = 'ssapp987'
    )
mail=Mail(app)

#initialize the app
mail.init_app(app)
bootstrap.init_app(app)
db.init_app(app)

#import models after creating db and email
from ssapp.models import *
from ssapp.views import *

