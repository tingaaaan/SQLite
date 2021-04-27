import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute(
    """
    CREATE TABLE students1 (
        name TEXT,
        addr TEXT,
        city TEXT,
        pin TEXT)
    """
    )
print("Table created successfully")
conn.close()
