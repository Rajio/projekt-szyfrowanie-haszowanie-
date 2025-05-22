import pytest
from src.aes import encrypt_aes, decrypt_aes
from Cryptodome.Random import get_random_bytes


def test_aes_encryption_decryption():
    key = get_random_bytes(16)
    data = b"Test AES encryption"
    nonce, ciphertext, tag = encrypt_aes(data, key)
    decrypted = decrypt_aes(nonce, ciphertext, tag, key)
    assert decrypted == data
