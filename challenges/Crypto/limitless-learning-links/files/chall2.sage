from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import random
import os
import hashlib

flag = b"SIVUSCG{REDACTED}"

p = getPrime(256)
a = random.randint(2024, 2^32)
b = random.randint(2024, a)

F = GF(p)

E = EllipticCurve(F, [a, b])
G = list(E.gens()[0])[:2]

print(f"{G = }")

secret = (str(a) + str(b)).encode()
key = hashlib.sha256(secret).digest()[:16]
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

ct = iv + cipher.encrypt(pad(flag, 16))
print(f"{p = }")
print(f"{ct = }")