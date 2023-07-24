import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base  # Use declarative_base from ext module
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean, unique=False, nullable=True, default=True)
    # planets_id = relationship('Planet', lazy=True)
    # people_id = relationship('People', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.email
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class UserFavorites(Base):
    __tablename__ = 'userfavorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    planets_id = relationship('Planet', lazy=True)
    people_id = relationship('People', lazy=True)
    def __repr__(self):
        return '<UserFavorites %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets": [planet.serialize() for planet in self.planets_id],
            "people": [person.serialize() for person in self.people_id],
            # do not serialize the password, its a security breach
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    mass = Column(Integer, unique=False, nullable=True)
    diameter = Column(Integer, unique=False, nullable=True)
    gravity = Column(Integer, unique=False, nullable=True)
    orbital_period = Column(Integer, unique=False, nullable=True)
    climate = Column(String(80), unique=False, nullable=True)
    terrain = Column(String(80), unique=False, nullable=True)
    favorite_planets = Column(Integer, ForeignKey(UserFavorites.id))
    def __repr__(self):
        return '<Planet %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "climate": self.climate,
            "terrain": self.terrain,
        }

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    gender = Column(String(80), unique=False, nullable=True)
    height = Column(Integer, unique=False, nullable=True)
    weight = Column(Integer, unique=False, nullable=True)
    age = Column(Integer, unique=False, nullable=True)
    race = Column(String(80), unique=False, nullable=True)
    hair_color = Column(String(80), unique=False, nullable=True)
    eye_color = Column(String(80), unique=False, nullable=True)
    favorite_people = Column(Integer, ForeignKey(UserFavorites.id))
    def __repr__(self):
        return '<People %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "age": self.age,
            "race": self.race,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
