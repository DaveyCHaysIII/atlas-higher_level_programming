#!/usr/bin/python3
"""write a script that lists all state objs
that contain letter 'a' from hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_states(username, password, db, search):
    mysql_local = ("mysql://{}:{}@localhost:3306/{}")
    engine = create_engine(mysql_local.format(username, password, db))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (session.query(City, State)
              .filter(City.state_id == State.id).all())

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

if __name__ == "__main__":
    username, password, db, search = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4])
    list_states(username, password, db, search)
