# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


from app import db, login_manager

from app.base.util import hash_pass

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None


# Static Tables (__init__.py file creates these tables and load csv files)
class Pregnancy(db.Model):
    __tablename__ = "Pregnancy"

    week = Column(Integer, primary_key=True)
    test = Column(String)
    opttest = Column(String)
    description = Column(String)
    datasource = Column(String)
    overview = Column(String)
    expectedsymptoms = Column(String)
    symptomdatasource = Column(String)
    babymilestones = Column(String)
    babysize = Column(String)
    babysizedatasource = Column(String)
    healthchecks = Column(String)
    conditions = Column(String)
    conditionsdescription = Column(String)
    symptoms = Column(String)
    tips = Column(String)

# Static Tables (__init__.py file creates these tables and load csv files)
class Tips(db.Model):
    __tablename__ = "Tips"

    week = Column(Integer, primary_key=True)
    vitamin = Column(String)
    description = Column(String)
    twins = Column(String)
    generaldietRecs = Column(String)
    mercurydietRecs = Column(String)
    mercurysafety = Column(String)
    painmedicine = Column(String)
    painwarining = Column(String)
    allergymedicine = Column(String)
    allergywarning = Column(String)
    antibioticsmedicine = Column(String)
    antibioticswarning = Column(String)
    stoolsoftnersmedicine = Column(String)
    stoolsoftnerswarning = Column(String)
    antacidsmedicine = Column(String)
    antacidswarning = Column(String)
    sleepaidmedicine = Column(String)
    sleepaidwarning = Column(String)

# Static Tables (__init__.py file creates these tables and load csv files)
class Prenatal(db.Model):
    __tablename__ = "Prenatal"

    week = Column(Integer, primary_key=True)
    title = Column(String)
    location = Column(String)
    time = Column(String)
    cost = Column(String)
    phonenumber = Column(String)
    datasource = Column(String)

# Static Tables (__init__.py file creates these tables and load csv files)
class Support(db.Model):
    __tablename__ = "Support"

    week = Column(Integer, primary_key=True)
    group = Column(String)
    description = Column(String)
    contactinfo = Column(String)
    depressiongroup = Column(String)
    depressioncontactinfo = Column(String)
    depressiondesc = Column(String)
    postpardumgroup = Column(String)
    postpardumcontactinfo = Column(String)
    postpardumdesc = Column(String)
    breastfeedgroup = Column(String)
    breastfeedcontactinfo = Column(String)
    breastfeeddesc = Column(String)
    poisoncontrolgroup = Column(String)
    poisoncontrolcontactinfo = Column(String)
    poisoncontroldesc = Column(String)


class Patient(db.Model):
    __tablename__ = "Patient"

    patient_id = Column(String, primary_key=True)
    first_Name = Column(String)
    last_Name = Column(String)
    middle_Name = Column(String)
    due_Date = Column(String)
    date_OfBirth = Column(String)
    date_Registered = Column(String)


class Patient_Symptoms(db.Model):
    __tablename__ = "Patient_Symptoms"

    patient_id = Column(String, primary_key=True)
    created_time = Column(String)
    updated_time = Column(String)
    has_Nausea = Column(String)
    has_StomachPain = Column(String)
    has_BodyAches = Column(String)
    has_MoodSwings = Column(String)
    has_Constipation = Column(String)
    has_ChestPain = Column(String)
    has_WeightGain = Column(String)
    has_Bloating = Column(String)


class HealthChecks(db.Model):
    __tablename__ = "HealthChecks"

    patient_id = Column(String, primary_key=True)
    week = Column(String)
    date_Completed = Column(String)
    date_Updated = Column(String)
    healthcheck_Name = Column(String)


class Login(db.Model):
    __tablename__ = "Login"

    email = Column(String, primary_key=True)
    password = Column(String)
    patient_id = Column(String)



def getstaticdata(table, week):
    db = SQLAlchemy()
    con = db.create_engine('sqlite:///db.sqlite3', {})
    table = str(table).upper()

    if table == "TIPS":
        results = con.execute("SELECT * FROM TIPS WHERE week = :week", {'week': week})

    if table == "PREGNANCY":
        results = con.execute("SELECT * FROM PREGNANCY WHERE week = :week", {'week': week})

    if table == "SUPPORT":
        results = con.execute("SELECT * FROM SUPPORT WHERE week = :week", {'week': week})

    if table == "PRENATAL":
        results = con.execute("SELECT * FROM PRENATAL WHERE week = :week", {'week': week})

    results = results.fetchall()

    #print(results)

    return results





