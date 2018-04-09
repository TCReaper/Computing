
import sqlite3

connection = sqlite3.connect('gunshop.db')

connection.execute("create table Weapons(ID INTEGER PRIMARY KEY, Name TEXT)")

weapondb = ['Heckler & Koch 416','Steyr SSG 08','AK-74',
            'Desert Eagle .50cal','Remington 887','FAMAS',
            'Dragunov SVD','CheyTac Intervention-American']

for weapon in weapondb:
      connection.execute("Insert into Weapons(Name) "+
                         "VALUES('"+weapon+"')")

connection.commit()
connection.close()
