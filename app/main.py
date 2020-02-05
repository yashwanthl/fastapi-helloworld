from fastapi import FastAPI
import uvicorn
from modules.dataset import Dataset
from modules.model import Model

app = FastAPI(title="Hello World", version='1.0', description="This is my Hello world application of FastAPI")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/train")
def train(modelname: str):
    ds = Dataset()
    emails = ds.get_data()
    md = Model()
    md.train(emails)
    md.serialize(modelname)
    return {"Hello": "World"}

@app.get("/predict")
def predict(emailtext: str, modelname: str):
    md = Model.deserialize(modelname)
    predict = md.predict([emailtext])
    if (predict[0] == 0):
        return {"SPAM": "NO"}
    if (predict[0] == 1):
        return {"SPAM": "YES"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    # Use the below line if you want to specify the port and/or host
    uvicorn.run(app, port=8080, host="0.0.0.0")