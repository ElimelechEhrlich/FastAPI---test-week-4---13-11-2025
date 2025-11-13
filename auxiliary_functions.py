from pydantic import BaseModel
from string import ascii_letters, ascii_lowercase, ascii_uppercase

class CaesarCipherItem(BaseModel):
    text: str
    offset: int 
    mode: str

class FenceCipherDecrypt(BaseModel):
    text: str

def names_file(name):
    with open('names.txt', 'a') as n:
        n.write(f'\n{name}')


def caesar_cipher_encrypt(text, offset):
    lowercase = [letter for letter in ascii_lowercase]
    uppercase = [letter for letter in ascii_uppercase]
    encrypt_text = ''
    for singl in text: 
        if singl.islower():
            encrypt_text += lowercase[(lowercase.index(singl) + offset) % 26]
        elif singl.isupper():
            encrypt_text += uppercase[(uppercase.index(singl) + offset) % 26]
        else:
            pass
    return {"encrypted_text": encrypt_text}

def caesar_cipher_decrypt(text, offset):
    lowercase = [letter for letter in ascii_lowercase]
    uppercase = [letter for letter in ascii_uppercase]
    decrypt_text = ''
    for singl in text: 
        if singl.islower():
            decrypt_text += lowercase[(lowercase.index(singl) - offset) % 26]
        elif singl.isupper():
            decrypt_text += uppercase[(uppercase.index(singl) - offset) % 26]
        else:
            pass
    return {"decrypted_text": decrypt_text}

def caesar_cipher(item:dict):
    if item['mode'] == 'encrypt':
        return caesar_cipher_encrypt(item['text'], item["offset"])
    elif item['mode'] == 'decrypt':
        return caesar_cipher_decrypt(item['text'], item["offset"])
    else:
        return {"error": "mode is only encrypt or decrypt"}
    

def fence_cipher(text):
    double = ''
    oddnumbers = ''
    for i in range(len(text)):
        if text[i] == ' ':
            text.remove(text[i])
    for i in range(len(text)):
        if i % 2 == 0:
            double += text[i]
        elif i % 2 != 0:
            oddnumbers += text[i]
    encrypt_text = double + oddnumbers
    return {"encrypted_text": encrypt_text}
    


def fence_cipher_decrypt(text):
    decrypt_text = ''
    a = int((len(text))/2)
    for i in range((len(text))/2):
        decrypt_text += text[i]
        decrypt_text += text[a]
        a += 1
    return {"decrypted": decrypt_text}

