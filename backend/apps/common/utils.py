import hashlib
import time


def generate_hash_id(*values: str) -> str:
    base = "_".join(values) + str(time.time())
    return hashlib.sha256(base.encode()).hexdigest()
