#!/usr/bin/python3
"""The State class."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, MetaData, Column
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """A State class that has the attributes id and name."""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    city = relationship("City", backref="states")
