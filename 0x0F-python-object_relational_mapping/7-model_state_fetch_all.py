#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa.

This script connects to a MySQL server running on localhost at port 3306
and retrieves all State objects from the specified database. The results
are sorted in ascending order by states.id.

Usage: ./script.py <mysql_username> <mysql_password> <database_name>
"""

# Import necessary modules
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

# this stop the code from executing if imported
if __name__ == "__main__":
    # Construct the database connection string
    db_connection_string = \
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    # Create the SQLAlchemy engine
    engine = create_engine(db_connection_string, pool_pre_ping=True)

    # Create all tables in the database (if they do not exist already)
    Base.metadata.create_all(engine)

    # Create a sessionmaker instance
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Retrieve all State objects and print them
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")

    finally:
        # Close the session
        session.close()

    # Dispose of the engine
    engine.dispose()
