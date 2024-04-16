#!/usr/bin/python3
#  a script that lists all states from the database hbtn_0e_0_usa:

import sys
import MySQLdb

if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row}")
