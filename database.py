import sqlite3
def create_table();
conn = sqlite3.connect("Employees.db")
cursor.execute('''
               CREATE TABLE IF NOT  IF NOT EXITS Employees(
            id TEXT PRIMARY KEY,
            name TEXT,
            role TEXT,
            gender TEXT,status TEXT       
               )''')
conn.commit()
conn.close()
def fetch_employees():
    conn = sqlite3.connect(Employees.db)
    
