#
# Built from SQLite3 tutorial https://docs.python.org/2/library/sqlite3.html
#

# SQLite Imports
import sqlite3
from sqlite3 import Error

# FHIR Model Imports
import fhirclient.models.patient as p
import fhirclient.models.humanname as hn
import fhirclient.models.observation as o
import fhirclient.models.datetime as dt

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_connection = None
    try:
        db_connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return db_connection


def write_symptoms(db_connection, symptoms):
    """
    Write symptoms into Patient_Symptoms table
    symptoms example = ('my_ID', '36', '2020-10-26', '2020-10-28', 'True', 'False', 'False', 'True', 'True', 'True', 'True', 'False')
    :return: symptoms entry row id
    """

    sql = ''' INSERT INTO Patient_Symptoms(patient_id,week,created_time,updated_time,has_Nausea,has_StomachPain,has_BodyAches,has_MoodSwings,has_Constipation,has_ChestPain,has_WeightGain,has_Bloating)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cursor = db_connection.cursor()
    cursor.execute(sql, symptoms)
    db_connection.commit()
    return cursor.lastrowid


def update_symptoms(db_connection, symptoms_update):
    """
    Update symptoms in Patient_Symptoms table
    symptoms_update example = ('2020-10-19', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'False', 'my_ID', 'week')
    :return: patient row id
    """

    sql = ''' UPDATE Patient_Symptoms
              SET updated_time = ? ,
                  has_Nausea = ? ,
                  has_StomachPain = ?,
                  has_BodyAches = ?,
                  has_MoodSwings = ?,
                  has_Constipation = ?,
                  has_ChestPain = ?,
                  has_WeightGain = ?,
                  has_Bloating = ?
              WHERE patient_id = ?
              AND week = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, symptoms_update)
    db_connection.commit()


def read_symptoms(db_connection, patient_id, week):
    """
    returns a tuple of symptoms: (patient_id,week,created_time,updated_time,has_Nausea,has_StomachPain,has_BodyAches,has_MoodSwings,has_Constipation,has_ChestPain,has_WeightGain,has_Bloating)
    """
    sql = '''SELECT * FROM Patient_Symptoms
            WHERE patient_id = ?
            AND week = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, (patient_id, week))
    response = cursor.fetchone()
    return response


def write_healthchecks(db_connection, healthChecks):
    """
    Write health checks into HealthChecks table
    healthChecks example = ('my_ID', '35', 2020-10-21', '2020-10-22', '2020-10-28', 'Ultrasound')
    :return: symptoms entry row id
    """

    sql = ''' INSERT INTO HealthChecks(patient_id,week,date_Completed,date_Updated,healthcheck_Name)
              VALUES(?,?,?,?,?) '''
    cursor = db_connection.cursor()
    cursor.execute(sql, healthChecks)
    db_connection.commit()
    return cursor.lastrowid


def update_healthchecks(db_connection, healthChecks_update):
    """
    Update healthchecks in HealthChecks table
    symptoms_update example = ('2020-20-19', 2020-10-19', 'my_ID', '34', 'Rh Test')
    :return: patient row id
    """

    sql = ''' UPDATE HealthChecks
              SET date_Completed = ?,
                  date_Updated = ?
              WHERE patient_id = ?
              AND week = ?
              AND healthcheck_Name = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, healthChecks_update)
    db_connection.commit()


def read_healthchecks(db_connection, patient_id, week):
    """
    returns a tuple of healthchecks data: (patient_id,week,date_Completed,date_Updated,healthcheck_Name)
    """
    sql = '''SELECT * FROM HealthChecks
            WHERE patient_id = ?
            AND week = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, (patient_id, week))
    response = cursor.fetchone()
    return response


def write_patient(db_connection, patient):
    """
    Write new patient into Patient table
    patient example = ('my_ID', 'Vinay', 'Vadlamudi', 'Kumar', '2020-10-16', '1990-07-23', '2020-10-01')
    :return: patient row id
    """

    sql = ''' INSERT INTO Patient(patient_id,first_Name,last_Name,middle_Name,due_Date,date_OfBirth,date_Registered)
              VALUES(?,?,?,?,?,?,?) '''
    cursor = db_connection.cursor()
    cursor.execute(sql, patient)
    db_connection.commit()
    return cursor.lastrowid


def update_patient(db_connection, patient_update):
    """
    Update patient in Patient table
    patient_update example = ('Vinay', 'Vadlamudi', 'Kumar', '2020-10-16', '1990-07-23', '2020-10-01', 'my_ID')
    :return: patient row id
    """

    sql = ''' UPDATE Patient
              SET first_Name = ? ,
                  last_Name = ? ,
                  middle_Name = ?,
                  due_date = ?,
                  date_OfBirth = ?
              WHERE patient_id = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, patient_update)
    db_connection.commit()


def read_patient(db_connection, patient_id):
    """
    returns a tuple of patient data: (patient_id,first_Name,last_Name,middle_Name,due_Date,date_OfBirth,date_Registered)
    """
    sql = '''SELECT * FROM Patient
            WHERE patient_id = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, (patient_id,))
    response = cursor.fetchall()
    return response


def export_records(db_connection, patient_id):
    """
    Export all patient records as Patient and Observation resources
    in FHIR JSON
    patient_id example = 123eir830dk8sjd73m
    return: nothing, saves JSON files
    """

    # ----------------------------------------- Patient Section ----------------------------------------- #

    output_file_Patient = open("./myData/patient/patient.txt", "w")

    sql = '''SELECT * FROM Patient
            WHERE patient_id = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, (patient_id,))
    response = cursor.fetchone()

    # response format: (patient_id,first_Name,last_Name,middle_Name,due_Date,date_OfBirth,date_Registered)

    # Extract each variable from the row
    p_id = response[0]
    p_firstName = response[1]
    p_lastName = response[2]
    p_middleName = response[3]
    p_dueDate = response[4]
    p_birthDate = response[5]
    p_registeredDate = response[6]


    #
    # TODO: Add variables to a FHIR Patient resource here
    #

    patient = p.Patient({'id': patient_id})

    name = hn.HumanName()
    name.given = [p_firstName, p_middleName]
    name.family = p_lastName
    patient.name = [name]
    patient.birthDate = p_birthDate

    output_file_Patient.write(patient.as_json())
    output_file_Patient.close()


     # ----------------------------------------- Observation Section ----------------------------------------- #
     # TODO: Add vital sign functionality

    sql = '''SELECT * FROM Patient_Symptoms
            WHERE patient_id = ?'''
    cursor.execute(sql, (patient_id,))
    response = cursor.fetchall()

    # response format [List]: (patient_id,week,created_time,updated_time,has_Nausea,has_StomachPain,has_BodyAches,has_MoodSwings,has_Constipation,has_ChestPain,has_WeightGain,has_Bloating)

    for row in response:
        # extract each variable from the row
        p_id = response[0]
        o_week = response[1]
        o_createdTime = response[2]
        o_updatedTime = response[3]
        o_hasNausea = response[4]
        o_hasStomachPain = response[5]
        o_hasBodyAches = response[6]
        o_hasMoodSwings = response[7]
        o_hasConstipation = response[8]
        o_hasChestPain = response[9]
        o_hasWeightGain = response[10]
        o_hasBloating = response[11]

        o_list = [o_hasNausea, o_hasStomachPain, o_hasBodyAches, o_hasMoodSwings, o_hasConstipation, o_hasChestPain, o_hasWeightGain, o_hasBloating]
        o_tags = ["nausea", "stomach pain", "body aches", "mood swings", "constipation", "chest pain", "weight gain", "bloating"]

        # make observation for each symptom present
        for i in range len(o_list):
            if o_list[i] == True:
                # add variable to a FHIR Observation resource
                observation = o.Observation()
                observation.subject = patient
                observation.valueString = o_tags[i]
                observation.valueString = o_list[i]   # should always be true
                # TODO: Maybe add LOINC Codes?
                observation.issued = o.created_time
                observation.effectiveDateTime = o.created_time

                output_file_Observation = open("./myData/observations/symptoms_week-" + o_week + "-" + o_tags[i], "w")
                output_file_Observation.write(observation.as_json())
                output_file_Observation.close()