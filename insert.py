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

#sintassi per inserire le tuple
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

#esegue il comando
mycursor.executemany(sql, val)

#applica le modifiche apportate al database, le salva
mydb.commit()

#restituisce il numero di righe modificate
print(mycursor.rowcount, "record inserted.")
