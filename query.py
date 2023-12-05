import mysql.connector

#configurazione per la connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

#cursore che ci permette di eseguire i comandi su mysql
mycursor = mydb.cursor()

#sintassi per eseguire una query
mycursor.execute("SELECT * FROM customers")

#restituisce tutta la lista di tuple
myresult = mycursor.fetchall()

#stampa le tuple restituite
for x in myresult:
  print(x)