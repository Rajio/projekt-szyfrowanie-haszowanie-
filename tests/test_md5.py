from src.md5 import hash_md5

def test_md5_hash():
    data = b"Test data"
    hashed = hash_md5(data)
    assert isinstance(hashed, str)
    assert len(hashed) == 32  # MD5 hash length in hex
