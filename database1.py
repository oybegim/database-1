import sqlite3 as sql

a = sql.connect("Telefonlar.db")

b =a.cursor()

b.execute("""
CREATE TABLE IF NOT EXISTS Redmi(
    xotira INTEGER,
    dastur TEXT
)
""")

b.execute(""" 
CREATE TABLE IF NOT EXISTS Samsung(
    dastur TEXT,
    xotira INTEGER
)
""")