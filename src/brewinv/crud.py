from typing import List
from sqlalchemy.orm import Session
from . import models, schemas


def get_ingredients(db: Session, skip: int = 0, limit: int = 100) -> List[models.Ingredient]:
    return db.query(models.Ingredient).offset(skip).limit(limit).all()


def create_ingredient(db: Session, ingredient: schemas.IngredientCreate):
    db_ingredient = models.Ingredient(**ingredient.dict())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)

    return db_ingredient