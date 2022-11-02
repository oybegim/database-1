import sqlite3 as sql

ozgaruvchi1 = sql.connect("Projectlar.db")

ozgaruvchi2 =ozgaruvchi1.cursor()

ozgaruvchi2.execute("""
CREATE TABLE IF NOT EXISTS Maktab(
    maydon INTEGER,
    xona INTEGER
)
""")

ozgaruvchi2.execute(""" 
CREATE TABLE IF NOT EXISTS Institut(
    fakultet TEXT,
    xona INTEGER
)
""")