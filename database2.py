import sqlite3 as sql

qiymat1 = sql.connect("Oquvchilar.db")

qiymat2 =qiymat1.cursor()

qiymat2.execute("""
CREATE TABLE IF NOT EXISTS Talaba(
    yosh INTEGER,
    ism TEXT
)
""")

qiymat2.execute(""" 
CREATE TABLE IF NOT EXISTS Abituriyent(
    familiya TEXT,
    yosh INTEGER
)
""")