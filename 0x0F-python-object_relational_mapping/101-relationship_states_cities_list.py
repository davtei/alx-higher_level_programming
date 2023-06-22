#!/usr/bin/python3
"""A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in (session.query(State).order_by(State.id)):
        print(instance.id, instance.name, sep=": ")
        for city_instance in instance.cities:
            print("    ", end="")
            print(city_instance.id, city_instance.name, sep=": ")
