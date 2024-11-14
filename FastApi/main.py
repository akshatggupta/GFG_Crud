from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the data model
class Item(BaseModel):
    id: int
    name: str
    address: str

# Sample data in dict - Fixed dictionary format
items = {
    1: {"id": 1, "name": "John", "address": "New York"},
    2: {"id": 2, "name": "Doe", "address": "California"},
    3: {"id": 3, "name": "Smith", "address": "Texas"},
    4: {"id": 4, "name": "David", "address": "Florida"}
}

# CRUD operations
# Get all items
@app.get("/items")
def get_all_items():
    return items

# Get single item
@app.get("/items/{item_id}")
def get_item(item_id: int):    #item_id is passed as parameter(as int type Fastapi Feture) 
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")   #throw error if item not found
    return items[item_id]

# Add new item
@app.post("/items")
def add_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item ID already exists")  #throw error if item already exists
    items[item.id] = item.dict()
    return items[item.id]
    

# Update item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")  #throw error if item not found
    items[item_id] = item.dict()
    return items[item_id]

# Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"message": f"Item {item_id} deleted", "deleted_item": deleted_item}