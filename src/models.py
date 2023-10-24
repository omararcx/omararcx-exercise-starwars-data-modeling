import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id=Column(Integer(), primary_key=True)
    username=Column(String(30), nullable=False, unique=True)
    name =Column(String(80), nullable=False)
    lastname=Column(String(80), nullable=False)
    age=Column(Integer(), nullable=True)
    email=Column(String(80), nullable=True)
    country=Column(String(60), nullable=True)
    favorites = relationship("Favorite", uselist=True, backref='users')


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id=Column(Integer(), primary_key=True)
    name =Column(String(80), nullable=False)
    speed=Column(Integer(), nullable=True)
    cost=Column(Integer(), nullable=True)
    cargo=Column(Integer(), nullable=True)
    passengers=Column(Integer(), nullable=True)
    favorites =relationship("Favorite", ForeignKey("favorites.id"))


class Person(Base):
    __tablename__ = 'people'
    id=Column(Integer(), primary_key=True)
    name =Column(String(80), nullable=False)
    side=Column(String(30), nullable=True)
    status=Column(String(30), nullable=True)
    origin=Column(String(30), nullable=True)
    favorites=relationship("Favorite", ForeignKey("favorites.id"))


class Planet(Base):
    __tablename__= "planets"
    id=Column(Integer(), primary_key=True, nullable=False)
    name=Column(String(150), nullable=False)
    population=Column(Integer(), nullable=True)
    controled=Column(String(150), nullable=True)
    favorites=relationship("Favorite", ForeignKey("favorites.id"))

class Favorite(Base):
    __tablename__ = 'favorites'
    id=Column(Integer(), primary_key=True)
    user_id=Column(Integer(),ForeignKey("users.id"))
    planet_id=Column(Integer(),ForeignKey("planets.id"))
    vehicle_id=Column(Integer(),ForeignKey("vehicles.id"))
    people_id=Column(Integer(),ForeignKey("people.id"))



#  class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
