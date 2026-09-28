import random
import string
from datetime import datetime

def random_username(prefix = "user"):
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{suffix}"

def random_password(length = 10):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

def random_email():
    return f"{random_username()}@example.com"

def now_str():
    return datetime.now().strftime("%Y%m%d%H%M%S")