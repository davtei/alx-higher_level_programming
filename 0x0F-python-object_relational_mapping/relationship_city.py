#!/usr/bin/python3
"""The City class."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    """A City class that has the attributes id, name, and state_id."""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
