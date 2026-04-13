from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db, engine, Base
from db.seed import seed_db
from db.models import Base
from db.schemas import Tariff, Delivery

from functions import functions
from exceptions.hooks import exception_handlers


def create_tables():
    Base.metadata.create_all(bind=engine)


app = FastAPI(title="automation-exam-kabashov")


for exception, handler in exception_handlers.items():
    app.add_exception_handler(exception, handler)


@app.on_event("startup")
def on_startup():
    create_tables()
    seed_db()


@app.get("/")
def read_root():
    return {"message": "automation-exam-kabashov: root"}


@app.get("/tariffs/", response_model=List[Tariff])
def get_tariffs(db: Session = Depends(get_db)):
    return functions.get_tariffs(db)    


@app.get("/delivery/{phone}/{id}", response_model=Delivery)
def get_delivery(phone: str, id: int, db: Session = Depends(get_db)):
    return functions.get_delivery(db, phone, id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
