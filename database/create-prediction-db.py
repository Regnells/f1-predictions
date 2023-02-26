import sqlite3

# Create Tables for Rasmus, Martin, Anton and Jesper

# Create a database connection
def create_db():
    conn = sqlite3.connect("database/pre-season-preciction.db")
    # Create a cursor
    c = conn.cursor()

    # Create a table
    c.execute("CREATE TABLE IF NOT EXISTS jesper (id INTEGER PRIMARY KEY, constructor TEXT, driver TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS anton (id INTEGER PRIMARY KEY, constructor TEXT, driver TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS martin (id INTEGER PRIMARY KEY, constructor TEXT, driver TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS rasmus (id INTEGER PRIMARY KEY, constructor TEXT, driver TEXT)")

    # Insert data into the tables
    for i in range(0, 10):
        c.execute("INSERT INTO jesper (id) VALUES (?)", (i,))
        c.execute("INSERT INTO anton (id) VALUES (?)", (i,))
        c.execute("INSERT INTO martin (id) VALUES (?)", (i,))
        c.execute("INSERT INTO rasmus (id) VALUES (?)", (i,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()