import sqlite3

def connect_db():
    connect = sqlite3.connect('User_data.db')
    return connect
 
def initialize_db():
    connect = connect_db()
    cur = connect.cursor()
 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS current_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            building TEXT NOT NULL,
            trip_type TEXT NOT NULL,
            miles INTEGER NOT NULL,
            cost REAL NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
         ''')
 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS archive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            building TEXT NOT NULL,
            trip_type TEXT NOT NULL,
            miles INTEGER NOT NULL,
            cost REAL NOT NULL,
            archived_on TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')
 
   
    connect.commit()
    connect.close()
 
initialize_db()