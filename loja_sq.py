import sqlite3

loja = sqlite3.connect('loja.db')

cursor = loja.cursor()

# cursor.execute("SELECT cliente,produto FROM vendas ")
# cursor.execute("SELECT produto FROM vendas WHERE cliente = 'João'")
cursor.execute("SELECT produto FROM vendas WHERE preco_unitario > 50")
print('--------------------------------------------------------------------------------------------------------------')
print(cursor.fetchall())
print('--------------------------------------------------------------------------------------------------------------')