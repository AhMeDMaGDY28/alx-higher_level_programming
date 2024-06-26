#!/usr/bin/python3
"""
 a script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
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

    # a var for the name which we will get inputed
    name = argv[4]

    # the sql formula which going to be excuted
    Sql_Formula = f"\
    SELECT * FROM states\
    WHERE states.name LIKE BINARY '{name}'\
    ORDER BY states.id"

    # the excute command to excute the formula
    cursor.execute(Sql_Formula)

    # fecthing all the data
    DATA_fetched_Rows = cursor.fetchall()

    # printing the data
    for data_row in DATA_fetched_Rows:
        print(data_row)

    # closing the cursor
    cursor.close()

    # closing the connection
    Data_Base_connection.close()
