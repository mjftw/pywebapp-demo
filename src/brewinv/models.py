from sqlalchemy import Column, Integer, String, Enum

from .database import Base
from .enums import UnitsEnum, IngredientTypesEnum


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    brand = Column(String(50), index=True, default=None)
    type = Column(Enum(IngredientTypesEnum))
    amount = Column(Integer)
    amount_unit = Column(Enum(UnitsEnum))