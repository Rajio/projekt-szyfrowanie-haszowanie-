import time
from src.aes import encrypt_aes, decrypt_aes
from src.rsa import generate_keys, encrypt_rsa
from src.sha256 import hash_sha256
from src.md5 import hash_md5
from Cryptodome.Random import get_random_bytes

def test_performance():
    data = b"a" * 100000  # 100KB data

    # AES performance
    key = get_random_bytes(16)
    start = time.perf_counter()
    nonce, ciphertext, tag = encrypt_aes(data, key)
    end = time.perf_counter()
    print(f"AES encryption time: {end - start:.6f} seconds")

    # RSA performance (on smaller data)
    private_key, public_key = generate_keys()
    rsa_data = b"Test RSA" * 10
    start = time.perf_counter()
    encrypted = encrypt_rsa(rsa_data, public_key)
    end = time.perf_counter()
    print(f"RSA encryption time: {end - start:.6f} seconds")

    # SHA-256 performance
    start = time.perf_counter()
    hash_sha256(data)
    end = time.perf_counter()
    print(f"SHA-256 hashing time: {end - start:.6f} seconds")

    # MD5 performance
    start = time.perf_counter()
    hash_md5(data)
    end = time.perf_counter()
    print(f"MD5 hashing time: {end - start:.6f} seconds")
