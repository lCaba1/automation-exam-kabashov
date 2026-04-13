from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db, engine, Base
from db.seed import seed_db
from db.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


app = FastAPI(title="automation-exam-kabashov")


@app.on_event("startup")
def on_startup():
    create_tables()
    seed_db()


@app.get("/")
def read_root():
    return {"message": "automation-exam-kabashov: root"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
