#!/usr/bin/python3
"""
a script that changes the name of a State object
from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
Your code should not be executed when imported
"""

# Import necessary modules
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

# this stop the code from excuting if imported
if __name__ == "__main__":
    # Construct the database connection string
    DataBase_connection_Formula = (
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    )

    # Create the SQLAlchemy engine
    engine = create_engine(DataBase_connection_Formula, pool_pre_ping=True)

    # Create all tables in the database (if they do not exist already)
    Base.metadata.create_all(engine)

    # Create a sessionmaker instance
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Retrieve all State objects and print them

        wanted_to_update = session.query(State)\
        .filter_by(id=2)\
        .one_or_none()

        wanted_to_update.name = "New Mexico"

    finally:
        # Close the session
        session.commit()
        session.close()

    # Dispose of the engine
    engine.dispose()
