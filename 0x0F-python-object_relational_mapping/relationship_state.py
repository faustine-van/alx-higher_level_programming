#!/usr/bin/python3
"""
 - define class called State and define column used in into database
 - updated to represent a relationship with the class City

"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """define class State with column
       - id: id of each name of state
       - name: name of state
    """

    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)

    cities = relationship(
        "City", backref = "state", cascade = "all, delete-orphan"
        )
