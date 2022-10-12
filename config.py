from app import app
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
import mysql.connector


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='jags1234'
app.config['MYSQL_DATABASW_DB'] = 'cricketers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
