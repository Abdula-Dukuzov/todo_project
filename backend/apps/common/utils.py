import hashlib
import time


def generate_hash_id(*values: str) -> str:
    """
    Генерирует детерминированный hash-based ID
    без UUID, random и автоинкремента
    """
    base = "_".join(values) + str(time.time())
    return hashlib.sha256(base.encode()).hexdigest()
