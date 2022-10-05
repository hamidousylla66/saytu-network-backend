import psycopg2
from flask import Flask
from script.function import *
import jsonify, json, jsonpickle

app = Flask(__name__)
test = "ceci est un test()"
#export Flask_APP =

@app.route("/")
def home():
    return  test # "Hello Flask  on fait des tesst test"

#create_table_inventaire()
@app.route("/inventaire")
def table_inventaire():
    con = None
    #response = []
    try:
        con = connect()
        cur = con.cursor();
        cur.execute("SELECT * FROM inventaireglobal_ftth ;")
        response = cur.fetchall()
        #print("Response data is ok ...")
        cur.close()
        con.commit()
        return response
        #print("Database closed .....")
    except (Exception, psycopg2.DatabaseError) as error:
        print("The database error " + error )
    finally:
        if con is not None:
            con.close()
    #return response

# simple inventaire info
@app.route('/simpleinventaire')
def simpleinventaire():
    #data = []
    con = None
    try:
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM inventaireglobal_ftth ;")
        data = cur.fetchall()
        cur.close()
        con.commit()
        #return jsonpickle.encode(data)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return jsonpickle.encode(data)






if __name__ == '__main__':
    #create_table_inventaire()
    app.run(debug=True)

