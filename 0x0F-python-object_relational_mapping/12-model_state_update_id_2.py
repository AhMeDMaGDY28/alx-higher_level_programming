#!/usr/bin/python3

"""
A script to update a state name in the database.

Usage:
    ./update_state.py <username> <password> <database>

Arguments:
    username: The username to connect to the MySQL database.
    password: The password to connect to the MySQL database.
    database: The name of the MySQL database.

Example:
    ./update_state.py root password hbtn_0e_6_usa
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

    """Update the state name with id 2 to 'New Mexico'"""
    for state in session.query(State):
        if state.id == 2:
            state.name = "New Mexico"
            break

    """Commit the changes"""
    session.commit()
