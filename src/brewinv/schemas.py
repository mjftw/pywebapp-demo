from typing import Optional
from pydantic import BaseModel

from brewinv.enums import IngredientTypesEnum, UnitsEnum


class Ingredient(BaseModel):
    '''Ingredient attributes to provided on read'''
    id: int
    name: str
    brand: Optional[str]
    type: IngredientTypesEnum
    amount: int
    amount_unit: UnitsEnum

    class Config:
        orm_mode = True


class IngredientCreate(Ingredient):
    '''Ingredient attributes to provided on creation'''
    pass
