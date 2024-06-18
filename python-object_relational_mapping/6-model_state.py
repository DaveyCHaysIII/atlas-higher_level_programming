#!/usr/bin/python3
"""this is our first sqlalchemy file"""

import sys
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class State(Base):
    __tablename__ = "states"

    id = Column("id", Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column("name", String(128),
                  nullable=False)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    mysql_local = "mysql://{}:{}@localhost:3306/{}"

    engine = create_engine(mysql_local.format(username, password, db))
    Base.metadata.create_all(bind=engine)
