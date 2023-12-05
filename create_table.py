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

#sintassi per creare la tabella
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")