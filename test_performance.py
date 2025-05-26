import time
from src.aes import encrypt_aes, decrypt_aes
from src.rsa import generate_keys, encrypt_rsa
from src.sha256 import hash_sha256
from src.md5 import hash_md5
from Cryptodome.Random import get_random_bytes

def test_performance():
    data = b"a" * 100000  # 100KB data
    times = {}

    print("=== Test szybkości algorytmów ===")

    # AES
    key = get_random_bytes(16)
    start = time.perf_counter()
    nonce, ciphertext, tag = encrypt_aes(data, key)
    end = time.perf_counter()
    aes_time = end - start
    times['AES'] = aes_time
    print(f"AES encryption time: {aes_time:.6f} s")

    # RSA (na mniejszych danych)
    private_key, public_key = generate_keys()
    rsa_data = b"Test RSA" * 10
    start = time.perf_counter()
    encrypted = encrypt_rsa(rsa_data, public_key)
    end = time.perf_counter()
    rsa_time = end - start
    times['RSA'] = rsa_time
    print(f"RSA encryption time: {rsa_time:.6f} s")

    # SHA-256
    start = time.perf_counter()
    hash_sha256(data)
    end = time.perf_counter()
    sha256_time = end - start
    times['SHA-256'] = sha256_time
    print(f"SHA-256 hashing time: {sha256_time:.6f} s")

    # MD5
    start = time.perf_counter()
    hash_md5(data)
    end = time.perf_counter()
    md5_time = end - start
    times['MD5'] = md5_time
    print(f"MD5 hashing time: {md5_time:.6f} s")

    print("\n=== Porównanie szybkości (od najszybszego) ===")
    for name, t in sorted(times.items(), key=lambda x: x[1]):
        print(f"{name}: {t:.6f} s")

# Uruchomienie
if __name__ == "__main__":
    test_performance()
