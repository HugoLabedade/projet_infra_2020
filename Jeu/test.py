import pymysql
import socket

db = pymysql.connect("localhost", "root", "pd853!gf", "data_pykemon")

curseur = db.cursor()

curseur.execute("DESCRIBE pokemons")

curseur.execute("SELECT * FROM data_pykemon.pokemons")

for row in curseur.fetchall():
    print(row[0], row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])

db.close()


