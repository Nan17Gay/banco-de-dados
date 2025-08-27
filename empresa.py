import sqlite3

empresa = sqlite3.connect('empresa.db')

cursor = empresa.cursor()

cursor.execute("SELECT nome,salario FROM funcionarios ")
cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carla'")
cursor.execute("SELECT * FROM funcionarios WHERE departamento = 'TI'")
print('--------------------------------------------------------------------------------------------------------------')
print(cursor.fetchall())
print('--------------------------------------------------------------------------------------------------------------')