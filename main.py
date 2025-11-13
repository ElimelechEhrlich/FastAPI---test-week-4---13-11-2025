from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get("/test")
def get_test():
    return '{"msg": "hi from test"}'



if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)