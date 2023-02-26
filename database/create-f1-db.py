import sqlite3

# Create Tables for Rasmus, Martin, Anton and Jesper
# Create a database connection
def create_db():
    conn = sqlite3.connect("f1.db")
    # Create a cursor
    c = conn.cursor()

    # Create a table for Rasmus
    c.execute("""CREATE TABLE IF NOT EXISTS rasmus (
        id INTEGER PRIMARY KEY,
        raceName TEXT,
        winner TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fifth TEXT,
        sixth TEXT
    )""")
    # Create a table for Martin
    c.execute("""CREATE TABLE IF NOT EXISTS martin (
        id INTEGER PRIMARY KEY,
        raceName TEXT,
        winner TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fifth TEXT,
        sixth TEXT
    )""")
    # Create a table for Anton
    c.execute("""CREATE TABLE IF NOT EXISTS anton (
        id INTEGER PRIMARY KEY,
        raceName TEXT,
        winner TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fifth TEXT,
        sixth TEXT
    )""")
    # Create a table for Jesper
    c.execute("""CREATE TABLE IF NOT EXISTS jesper (
        id INTEGER PRIMARY KEY,
        raceName TEXT,
        winner TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fifth TEXT,
        sixth TEXT
    )""")
    # Create points table
    c.execute("""CREATE TABLE IF NOT EXISTS points (
        id INTEGER PRIMARY KEY,
        name TEXT,
        points INTEGER
    )""")

    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()

def insert_races():
    # Grand prix order
    race_1 = "Bahrain Grand Prix"
    race_2 = "Saudi Arabian Grand Prix"
    race_3 = "Australian Grand Prix"
    race_4 = "Azerbaijan Grand Prix"
    race_5 = "Miami Grand Prix"
    race_6 = "Emilia Romagna Grand Prix"
    race_7 = "Monaco Grand Prix"
    race_8 = "Spanish Grand Prix"
    race_9 = "Canadian Grand Prix"
    race_10 = "Austrian Grand Prix"
    race_11 = "Great Britain Grand Prix"
    race_12 = "Hungarian Grand Prix"
    race_13 = "Belgian Grand Prix"
    race_14 = "Dutch Grand Prix"
    race_15 = "Italian Grand Prix"
    race_16 = "Singapore Grand Prix"
    race_17 = "Japanese Grand Prix"
    race_18 = "Qatar Grand Prix"
    race_19 = "United States Grand Prix"
    race_20 = "Mexico Grand Prix"
    race_21 = "Brazilian Grand Prix"
    race_22 = "Las Vegas Grand Prix"
    race_23 = "Abu Dhabi Grand Prix"

    races = [race_1, race_2, race_3, race_4, race_5, race_6, race_7, race_8, race_9, race_10, race_11, race_12, race_13, race_14, race_15, race_16, race_17, race_18, race_19, race_20, race_21, race_22, race_23]

    for i in range(races):
        # Connect to the database
        conn = sqlite3.connect("f1.db")
        c = conn.cursor()
        # Insert data
        # switch name for each name
        c.execute("INSERT INTO jesper (id, raceName) VALUES (?, ?)", (i+1, races[i]))
        conn.commit()
        conn.close()

if __name__ == "__main__":
    #create_db()
    #insert_races()
    pass