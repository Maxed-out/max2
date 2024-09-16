from fastapi import FastAPI

app = FastAPI()

gpio=[]
gpio_name=[]
relays=[]
relay={"gpio":10,"name":"gpio10"}
relays.append(relay)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/relay/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]