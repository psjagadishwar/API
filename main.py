from operator import truediv
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/create', methods=['POST'])
def create_players():
    try:        
        _json = request.json
        _name = _json['name']
        _jerseyno = _json['jerseyno']
        _nationality = _json['nationality']
        _city = _json['city']
        _age = _json['age']


        if _name and _jerseyno and _nationality and _city and _age and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO emp(name, jerseyno, nationality, city, age) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_name, _jerseyno, _nationality, _city, _age)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Player added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          
     
@app.route('/players')
def players():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name, jerseyno, nationality, city, age FROM players")
        playersRows = cursor.fetchall()
        respone = jsonify(playersRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/players/')
def players_detail(players_jerseyno):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name, jerseyno, nationality, city, age FROM players WHERE id =%s", players_jerseyno)
        playersRow = cursor.fetchone()
        respone = jsonify(playersRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/update', methods=['PUT'])
def update_players():
    try:
        _json = request.json
        _name = _json['name']
        _jerseyno = _json['jerseyno']
        _nationality = _json['nationality']
        _city = _json['city']
        _age = _json['age']
        if _name and _jerseyno and _nationality and _city and _age and request.method == 'PUT':			
            sqlQuery = "UPDATE players SET name=%s, nationality=%s, city=%s, age=%s WHERE jerseyno=%s"
            bindData = (_name, _jerseyno, _nationality, _city, _age,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Player updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/delete', methods=['DELETE'])
def delete_players(jerseyno):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM players WHERE jerseyno =%s", (jerseyno,))
		conn.commit()
		respone = jsonify('Player deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(debug= True)