#!/usr/bin/python3
"""a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    state_name = argv[4]
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE states.name\
                 LIKE BINARY '{}' ORDER BY states.id".format(
            argv[4]
        )
    )
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
    cur.close()
    db.close()
