#!/usr/bin/python3
#  a script that lists all states from the database hbtn_0e_0_usa:

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row}")
