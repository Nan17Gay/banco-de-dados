import sqlite3

#cria a conexao com o banco e guarda na variavel 'banco'
banco = sqlite3.connect('banco.db')

#criamos a variavel cursor e colocamos em uma variavel
cursor = banco.cursor()

#cria a tabela pessoas com os campos necessarios
cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")

#inserindo na tabela desejada os valores
cursor.execute("INSERT INTO pessoas VALUES('Ana',17,'usuariodedougl45@gmail.com')")

#enviando os dados
banco.commit()

#printar a informação
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())