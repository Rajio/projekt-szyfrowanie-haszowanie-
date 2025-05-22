from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def encrypt_aes(data: bytes, key: bytes) -> tuple:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, ciphertext, tag

def decrypt_aes(nonce: bytes, ciphertext: bytes, tag: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data
