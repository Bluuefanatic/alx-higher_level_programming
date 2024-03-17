#!/usr/bin/python3
"""Defines the City class."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """The City class inherits from Base.
    Links to the MySQL table cities.
    Attributes:
        id (Column): Represents a column of an auto-generated, unique integer, can't be null and is a primary key.
        name (Column): Represents a column of a string with maximum 128 characters and can't be null.
        state_id (Column): Represents a column of an integer, can't be null and is a foreign key to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
