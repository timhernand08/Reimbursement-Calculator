import sqlite3
from Travel import Building


def create_entry(building: Building):
    connect = sqlite3.connect('User_data.db')
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO current_db (building, trip_type, miles, cost) VALUES (:building, :triptype, :miles, :cost)"""
                   , {'building': building.building, 'triptype':building.tripType, 'miles':building.miles, 'cost':building.cost})
    connect.commit()
    connect.close()

def get_current_data():
    connect = sqlite3.connect('User_data.db')
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM current_db""")
    data = cursor.fetchall()
    connect.close()
    return data