import enum


class IngredientTypesEnum(enum.Enum):
    hops = 'hops'
    malts = 'malts'
    yeast = 'yeast'
    water = 'water'
    misc = 'misc'


class UnitsEnum(enum.Enum):
    milliliters = 'ml'
    liters = 'l'
    grams = 'g'
    kilograms = 'kg'