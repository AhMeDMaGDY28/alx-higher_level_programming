#!/usr/bin/python3

"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    Connect to the database
    """
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    """
    Get the state name from the command line argument
    """
    state_name = argv[4]

    """
    Check if the state name is a single word
    """
    if len(state_name.split()) == 1:
        """
        Create a cursor
        """
        with db_connection.cursor() as cursor:
            """
            Execute query using a parameterized query
            """
            cursor.execute(
                "SELECT cities.name FROM cities \
                WHERE state_id IN \
                     (SELECT id FROM states WHERE name LIKE BINARY %s) \
                     ORDER BY cities.id",
                (state_name,),
            )

            """
            Fetch all rows
            """
            rows = cursor.fetchall()

            """
            Print cities
            """
            if len(rows) == 0:
                print()
            else:
                for i in range(0, len(rows)):
                    if i == (len(rows) - 1):
                        print(f"{rows[i][0]}")
                    else:
                        print(f"{rows[i][0]}", end=", ")

    """
    Close the database connection
    """
    if db_connection:
        db_connection.close()
