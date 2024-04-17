#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username,
mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""
# to use the argv from the system when running the code
from sys import argv

# to use database with python
import MySQLdb


# this stop the code from excuting if imported
if __name__ == "__main__":
    # Connect to the database
    Data_Base_connection = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    # making a cursor using the connection
    cursor = Data_Base_connection.cursor()

    # to stop the mysql injection
    if len(argv[4].split()) == 1:
        # a var for the name which we will get inputed
        name = argv[4]

        # the sql formula which going to be excuted
        Sql_Formula = "\
        SELECT cities.name FROM cities\
        WHERE state_id IN \
        (SELECT id FROM states WHERE name LIKE BINARY %s)\
        ORDER BY cities.id"

        # the excute command to excute the formula
        cursor.execute(Sql_Formula, (f"%{name}%",))

        # fecthing all the data
        DATA_fetched_Rows = cursor.fetchall()

        # printing the data
        if len(DATA_fetched_Rows) == 0:
            print()
        else:
            # extracting city names from the fetched data
            city_names = [row[0] for row in DATA_fetched_Rows]

            # concatenating city names with commas
            city_names_str = ", ".join(city_names)

            # printing the concatenated string
            print(city_names_str)

        # closing the cursor
        cursor.close()

        # closing the connection
        Data_Base_connection.close()
