import mysql.connector

#configurazione per la connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

#cursore che ci permette di eseguire i comandi su mysql
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")