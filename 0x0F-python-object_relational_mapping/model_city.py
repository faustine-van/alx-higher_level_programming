#!/usr/bin/python3
"""
define class called City and define column used in into database

"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """define class City with column
       - id: id of each name of state
       - name: name of state
       - state_id: id
    """
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
