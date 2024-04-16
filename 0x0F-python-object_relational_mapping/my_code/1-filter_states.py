#!/usr/bin/python3
"""
a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
from sys import argv
import MySQLdb
"""
line 14: to use the argv from the system when running the code
line 15: to use database with python
this stop the code from excuting if imported"""
if __name__ == "__main__":
    """Connect to the database"""
    Data_Base_connection = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    """making a cursor using the connection"""
    cursor = Data_Base_connection.cursor()
    """the sql formula which going to be excuted"""
    Sql_Formula = "\
    SELECT * FROM states\
    WHERE states.name LIKE 'N%'\
         ORDER BY states.id"

    """the excute command to excute the formula"""
    cursor.execute(Sql_Formula)

    """fecthing all the data"""
    rows = cursor.fetchall()

    """printing the data"""
    for row in rows:
        print(row)

    """closing the cursor"""
    cursor.close()

    """closing the connection"""
    Data_Base_connection.close()
