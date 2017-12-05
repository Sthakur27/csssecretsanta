#this file creates the sqlite database if it doesn't already exist
#do not run if 'ss.db' is already in ssapp/
from ssapp.settings import SQLALCHEMY_DATABASE_URI
from ssapp.settings import SQLALCHEMY_MIGRATE_REPO
from ssapp import db
import os.path
db.create_all()

