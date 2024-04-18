#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


if getenv("HBNB_TYPE_STORAGE")=="db":
        
    class Amenity(BaseModel, Base):
        """class that represents Amenities in the system"""

        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        """class that represents Amenities in the system"""
        name=""
