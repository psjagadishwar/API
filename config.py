from app import app
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()
MYSQL_DATABASE_USER = os.getenv('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE_DB = os.getenv('MYSQL_DATABASE_DB')
MYSQL_DATABASE_HOST = os.getenv('MYSQL_DATABASE_HOST')

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] =MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = MYSQL_DATABASE_HOST
mysql.init_app(app)
