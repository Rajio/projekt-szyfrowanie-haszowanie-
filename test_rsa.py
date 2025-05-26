import pytest
from src.rsa import generate_keys, encrypt_rsa, decrypt_rsa

def test_rsa_encryption_decryption():
    private_key, public_key = generate_keys()
    data = b"Test RSA encryption"
    encrypted = encrypt_rsa(data, public_key)
    decrypted = decrypt_rsa(encrypted, private_key)
    assert decrypted == data
