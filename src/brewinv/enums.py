from enum import Enum


class IngredientTypesEnum(str, Enum):
    hops = 'hops'
    malts = 'malts'
    yeast = 'yeast'
    water = 'water'
    misc = 'misc'


class UnitsEnum(str, Enum):
    milliliters = 'ml'
    liters = 'l'
    grams = 'g'
    kilograms = 'kg'