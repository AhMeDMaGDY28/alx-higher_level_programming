#!/usr/bin/python3

"""
A script to retrieve and print the ID of a specific state from the database.

Usage:
    ./retrieve_state_id.py <username> <password> <database> <state_name>

Arguments:
    username:   The username to connect to the MySQL database.
    password:   The password to connect to the MySQL database.
    database:   The name of the MySQL database.
    state_name: The name of the state whose ID is to be retrieved.

Example:
    ./retrieve_state_id.py root password hbtn_0e_6_usa "California"
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    found = False

    for state in session.query(State):
        if state.name == state_name:
            print(state.id)
            found = True
            break

    if not found:
        print("Not found")
