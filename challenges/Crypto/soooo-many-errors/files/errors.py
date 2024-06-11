from fastapi import FastAPI
import random
import os
import math
from Crypto.Util.number import bytes_to_long
from secret import FLAG

app = FastAPI()

q = 401
e = 10
s = [ord(i) for i in FLAG]

def rand_poly():
    return [random.randint(0, q-1) for _ in range(len(FLAG))]

def rand_err():
    return math.floor(random.gauss(0, q/4/4))

def check_bounds(x, lower, upper):
    lower = lower % q
    upper = upper % q
    x = x % q
    if lower <= x <= upper:
        return True
    
    if upper < lower and lower <= x <= upper + q:
        return True
    
    if lower > upper and lower - q <= x <= upper:
        return True
    
    return False
    
def dot_mul(a, b):
    assert len(a) == len(b)
    ret = 0
    for i in range(len(a)):
        ret += a[i] * b[i] % q
    return ret % q

def dot_add(a, b):
    assert len(a) == len(b)
    ret = [0 for _ in range(len(a))]
    for i in range(len(a)):
        ret[i] = (a[i] + b[i]) % q
    return ret

def gen_key(n):
    samples = []
    for _ in range(n):
        p = rand_poly()
        x = dot_mul(p, s)
        samples.append((p, x))
    return samples

random.seed(FLAG)
secret_key = gen_key(50)
random.seed(os.urandom(16))

@app.post("/encrypt")
def encrypt(m: str):
    bits = bin(bytes_to_long(m.encode()))[2:]
    c = []
    for b in bits:
        if b == '1':
            cb = []
            for _ in range(e):
                ps = random.sample(secret_key, 2)
                p = dot_add(ps[0][0], ps[1][0])
                x = ps[0][1] + ps[1][1] + rand_err()
                cb.append((p, x))
            c.append(cb)
        elif b == '0':
            cb = []
            for _ in range(e):
                p = rand_poly()
                x = random.randint(0, q-1)
                cb.append((p, x))
            c.append(cb)
    return c

@app.get("/get_flag")
def get_flag():
    return encrypt(FLAG)