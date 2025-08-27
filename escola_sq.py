import sqlite3

escola = sqlite3.connect('escola.db')

cursor = escola.cursor()

# cursor.execute("SELECT nome,nota FROM alunos ")
# cursor.execute("SELECT * FROM alunos WHERE id = 3")
cursor.execute("SELECT nome FROM alunos WHERE turma = 'B' and nota > 7")
print('--------------------------------------------------------------------------------------------------------------')
print(cursor.fetchall())
print('--------------------------------------------------------------------------------------------------------------')