from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from auxiliary_functions import CaesarCipherItem, FenceCipherDecrypt, names_file, caesar_cipher, fence_cipher, fence_cipher_decrypt


app = FastAPI()

@app.get("/test")
def get_test():
    return '{"msg": "hi from test"}'

@app.get("/test/{name}")
def save_name(name):
    names_file(name)
    return '{"msg": "saved user"}'

@app.post("/caesar")
def pose_caesar_cipher(item:CaesarCipherItem):
    return caesar_cipher(item.__dict__)


@app.get("/fence/encrypt")
def get_fence(text:str):
    return fence_cipher(text)

@app.post("/fence/decrypt")
def pose_fence_cipher(item:FenceCipherDecrypt):
    return fence_cipher_decrypt(item.text)



   


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)