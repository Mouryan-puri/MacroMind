import sqlite3


connection=sqlite3.connect("meals.db")

curr=connection.cursor()

curr.execute("SELECT * FROM meals")

rows=curr.fetchall()

for i in rows:
    print(i, sep="\n\n")