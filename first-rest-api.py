import mysql.connector
from flask import Flask

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return result

@app.route("/air_transport")
def air_transport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport = 'Air'")
    air_units = mycursor.fetchall()
    result = []
    for i in air_units:
        result.append(i)
    return str(result)

@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = 'epic'")
    epic_units = mycursor.fetchall()
    result = []
    for i in epic_units:
        result.append(i)
    return str(result)

@app.route("/count")
def count():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Count = 'x1'")
    count = mycursor.fetchall()
    result = []
    for i in count:
        result.append(i)
    return str(result)

@app.route("/card_cost")
def cardCost():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost = '8'")
    cost = mycursor.fetchall()
    result = []
    for i in cost:
        result.append(i)
    return str(result)
    