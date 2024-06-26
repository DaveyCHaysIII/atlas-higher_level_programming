#!/usr/bin/python3
"""write a script that lists all state objs from hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db):
    mysql_local = ("mysql://{}:{}@localhost:3306/{}")
    engine = create_engine(mysql_local.format(username, password, db))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).first()

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db)
