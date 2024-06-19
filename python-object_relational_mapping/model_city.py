#!/usr/bin/python3
""" Write a base class for cities table """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """ City Class """
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
