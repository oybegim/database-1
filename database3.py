import sqlite3 as sql

malumot1 = sql.connect("Uylar.db")

malumot2 =malumot1.cursor()

malumot2.execute("""
CREATE TABLE IF NOT EXISTS Xovli(
    maydon INTEGER,
    joy TEXT,
    xona INTEGER
)
""")

malumot2.execute(""" 
CREATE TABLE IF NOT EXISTS Dom(
    joy TEXT,
    xona INTEGER
)
""")