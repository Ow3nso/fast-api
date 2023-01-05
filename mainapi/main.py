from typing import List

import sqltap
import uvicorn      
from fastapi import Depends, FastAPI, HTTPException
from starlette.requests import Request
from sqlalchemy.orm import Session

from .database import engine, SessionLocal

from . import models

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {'status': "success"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
"""
@app.on_event("startup")
async def reset_db():
    try:
        db = SessionLocal()
        print("deleting all items and users")
        db.query(models.Item).delete()
        db.query(models.User).delete()

        print("Populating users")
        for i in range(50):
            user = models.User(email=f"user{i}@email.com", hashed_password=f"pwdforuser{i}")
            db.add(user)
        db.commit()

        print("Populating items")
        users = db.query(models.User).filter()
        for user in users:
            for i in range(20):
                user_item = models.Item(title=f"Item{i}", description=f"Item{i} description", owner=user)
                db.add(user_item)
        db.commit()
    finally:
        db.close()


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

"""