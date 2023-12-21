import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

@app.route("/")
def hello():
    return "Hello, Worldb!"

'''
@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/air_transport")
def air_transport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport = 'Air'")
    air_units = mycursor.fetchall()
    result = []
    for i in air_units:
        result.append(i)
    return jsonify(result)

@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = 'epic'")
    epic_units = mycursor.fetchall()
    result = []
    for i in epic_units:
        result.append(i)
    return jsonify(result)

@app.route("/card_cost")
def cardCost():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost = '8'")
    cost = mycursor.fetchall()
    result = []
    for i in cost:
        result.append(i)
    return jsonify(result)

@app.route("/count")
def count():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Count = 'x1'")
    count = mycursor.fetchall()
    result = []
    for i in count:
        result.append(i)
    return jsonify(result)'''

@app.route('/count')
def count():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Count = 'x1'")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    count = mycursor.fetchall()
    json_data=[]
    for result in count:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for x in myresult:
        json_data.append(dict(zip(row_headers,x)))
    return jsonify(json_data)

@app.route("/air_transport")
def air_transport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport = 'Air'")
    row_headers=[x[0] for x in mycursor.description]
    air_units = mycursor.fetchall()
    json_data=[]
    for result in air_units:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = 'epic'")
    row_headers=[x[0] for x in mycursor.description]
    epic_units = mycursor.fetchall()
    json_data=[]
    for result in epic_units:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route("/card_cost")
def cardCost():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost = '8'")
    row_headers=[x[0] for x in mycursor.description]
    cost_units = mycursor.fetchall()
    json_data=[]
    for result in cost_units:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)