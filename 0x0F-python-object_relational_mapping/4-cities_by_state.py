#!/usr/bin/python3

"""a script that lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    database_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    cursor = database_connect.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities,\
                states WHERE cities.state_id = states.id ORDER BY\
                cities.id"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row}")
