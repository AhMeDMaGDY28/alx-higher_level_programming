#!/usr/bin/python3

"""
A script to print all cities with their respective states.

Usage:
    ./print_cities.py <username> <password> <database>

Arguments:
    username: The username to connect to the MySQL database.
    password: The password to connect to the MySQL database.
    database: The name of the MySQL database.

Example:
    ./print_cities.py root password hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
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

    """Query all cities with their respective states and print the results"""
    for state, city in (
        session.query(State, City).filter(State.id == City.state_id).
        order_by(City.id)
    ):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
