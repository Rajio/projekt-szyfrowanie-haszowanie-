from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP


def generate_keys(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(data: bytes, public_key: bytes) -> bytes:
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.encrypt(data)

def decrypt_rsa(ciphertext: bytes, private_key: bytes) -> bytes:
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(ciphertext)
