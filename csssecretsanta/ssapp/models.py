#creates an SQLalchemy ORM mapping of database tables
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from ssapp import db
########################################################################
#creates User class for users table
class User(db.Model):
    __tablename__="users" 
    id = db.Column(db.Integer, db.Sequence('user_seq',start=1,increment=1), primary_key=True)
    username = db.Column(db.String(25))
    email = db.Column(db.String(45))
    password = db.Column(db.String(25))
    wishlist=db.Column(db.String(400))
    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email=email

#creates Pool class for pools table
class Pool(db.Model):
    __tablename__="pools"
    id = db.Column(db.Integer,db.Sequence('pool_seq',start=1,increment=1), primary_key=True)
    name=db.Column(db.String(40))
    userinfo=db.Column(db.String(100000))
    description=db.Column(db.String(1000))
    def __init__(self,name,description,userinfo):
        self.name=name
        self.description=description
        self.userinfo=userinfo
