#!/usr/bin/python3
"""
Defines the State class using SQLAlchemy ORM.

The State class represents the 'states' table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The primary key ID of the state.
        name (str): The name of the state.
    """

    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    name = Column(String(128), nullable=False)
