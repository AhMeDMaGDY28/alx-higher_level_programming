#!/usr/bin/python3
"""A script to retrieve the first state
from the database and print its ID and name."""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""Retrieve the first state from the database
and print its ID and name."""
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
    result = session.query(State.id, State.name).first()
    if not result:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))
