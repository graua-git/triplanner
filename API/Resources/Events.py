# API Endpoints related to the Events table
from flask_restful import Api, Resource
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='triplannerdb'
)
cursor = connection.cursor()

class ReadEvents(Resource):
    def get(self):
        cursor.execute("SELECT * FROM Events")
        return cursor.fetchall()