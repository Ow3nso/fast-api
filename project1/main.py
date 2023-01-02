from typing import Optional, List
from fastapi import FastAPI, status
from database import SessionLocal
from pydantic import BaseModel
import models

app = FastAPI()
db = SessionLocal()

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class config:
        orm_mode=True


@app.get('/items',response_model=List[Item], status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get("/item/{item_id}")
def get_an_item(item_id:int):
    pass

'''
@app.post('/itemy', response_model=List,status_code=201)
def create_an_item(item:Item):
    new_item=models.Item(name=item.name,
                        price=item.price,
                        description=item.description,
                        on_offer=item.on_offer
                        )
    db.add(new_item)
    db.commit()

    return new_item
'''


@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete("/item/{item_id}")
def delete_item(item_id:int):
    pass