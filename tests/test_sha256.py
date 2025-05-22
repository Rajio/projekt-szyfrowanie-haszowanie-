from src.sha256 import hash_sha256

def test_sha256_hash():
    data = b"Test data"
    hashed = hash_sha256(data)
    assert isinstance(hashed, str)
    assert len(hashed) == 64  # SHA-256 hash length in hex
