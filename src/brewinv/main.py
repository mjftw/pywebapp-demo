from typing import Optional, List
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session

from brewinv.crud import get_ingredients

from . import crud, models, schemas
from .database import SessionLocal, engine, Base

#TODO: Switch to using Alembic for DB migrations
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def common_get_all_args(skip: int = 0, limit: int = 100):
    return {'skip': skip, 'limit': limit}


@app.get('/ingredients', response_model=List[schemas.Ingredient])
async def get_ingredients(commons: dict = Depends(common_get_all_args), db: Session = Depends(get_db)):
    return crud.get_ingredients(db=db, **commons)

@app.post('/ingredients', response_model=schemas.Ingredient)
async def create_ingredient(ingredient: schemas.IngredientCreate, db: Session =  Depends(get_db)):
    # Duplicate items allowed
    return crud.create_ingredient(db=db, ingredient=ingredient)
