#!/usr/bin/python3
"""
This script retrieves and prints all states from the specified database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    """
    Create all tables in the database
    """
    Base.metadata.create_all(engine)

    """
    Create a session to interact with the database
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query all states and print them
    """
    for id, name in session.query(State.id, State.name).order_by(State.id):
        print("{}: {}".format(id, name))
