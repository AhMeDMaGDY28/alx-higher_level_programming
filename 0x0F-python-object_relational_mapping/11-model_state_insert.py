#!/usr/bin/python3

"""
A script to add a new state to the database and retrieve its ID.

Usage:
    ./add_state.py <username> <password> <database>

Arguments:
    username: The username to connect to the MySQL database.
    password: The password to connect to the MySQL database.
    database: The name of the MySQL database.

Example:
    ./add_state.py root password hbtn_0e_6_usa
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

    """Add a new state to the database"""
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    """Retrieve the ID of the newly added state"""
    for state in session.query(State):
        if state.name == "Louisiana":
            print(state.id)
            break
