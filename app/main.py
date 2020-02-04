from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Hello World", version='1.0', description="This is my Hello world application of FastAPI")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    # Use the below line if you want to specify the port and/or host
    uvicorn.run(app, port=8000, host="0.0.0.0")