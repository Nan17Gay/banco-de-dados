import sqlite3

cinema = sqlite3.connect('cinema.db')

cursor = cinema.cursor()

# cursor.execute("SELECT titulo,genero FROM filmes ")
# cursor.execute("SELECT * FROM filmes WHERE titulo = 'Matrix'")
cursor.execute("SELECT titulo,avaliacao FROM filmes WHERE ano > 2010")
print('--------------------------------------------------------------------------------------------------------------')
print(cursor.fetchall())
print('--------------------------------------------------------------------------------------------------------------')