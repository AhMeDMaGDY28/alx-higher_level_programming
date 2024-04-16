#!/usr/bin/python3
"""A script to retrieve and print all states
with names containing 'a' from the database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Retrieve and print all states with
     names containing 'a' from the database."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = (
        session.query(State.id, State.name)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
    )
    if not result:
        print("Nothing")
    else:
        for id, name in result:
            print("{}: {}".format(id, name))
