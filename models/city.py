#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city for MySQL database.

    Inherits from SQLAlchemy Base and connects to the MySQL table cities.

    Attributes:
        __tablename__ (str):  name of MySQL table to store Cities.
        name (sqlalchemy String): name of the City.
        state_id (sqlalchemy String):state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
