from hashlib import blake2b, sha256
from time import time
from math import log
import random

def gen_hash():
    random.seed()
    return bytes.fromhex(blake2b(str(log(time(),random.random())).encode(), digest_size=4).hexdigest())
