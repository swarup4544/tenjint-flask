import random
import string

def generate_token(length=32):
    """
    generate token using hex chars
    Args:
        length: length of token - default 32
    Returns:
        token string
    """
    return "".join(random.choice("0123456789abcdef") for _ in range(32))