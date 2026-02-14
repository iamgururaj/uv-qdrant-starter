import hashlib


def make_id(text: str) -> int:
    return int(hashlib.md5(text.encode()).hexdigest(), 16) % (10**12)
