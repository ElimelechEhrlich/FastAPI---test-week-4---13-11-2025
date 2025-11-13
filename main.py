from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from auxiliary_functions import names_file

app = FastAPI()

@app.get("/test")
def get_test():
    return '{"msg": "hi from test"}'

@app.get("/test/{name}")
def save_name(name):
    names_file(name)
    return '{"msg": "saved user"}'

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)