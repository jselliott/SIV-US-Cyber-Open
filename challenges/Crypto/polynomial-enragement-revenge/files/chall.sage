from Crypto.Util.number import *
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from hashlib import sha256
import os

key = os.urandom(40)

flag = b"SIVUSCG{REDACTED}"

P.<x> = PolynomialRing(ZZ)

flag_poly = list(key)

f = 0
for i in range(len(flag_poly)):
	f += (x^i)*flag_poly[i]

g = P.random_element(degree=30)
h = P.random_element(degree=30)

noise1 = P.random_element(degree=10)
noise2 = P.random_element(degree=10)

poly1 = f*g + noise1
poly2 = f*h + noise2

print(poly1)
print(poly2)

cipher = AES.new(sha256(key).digest()[:16], AES.MODE_ECB)
ct = cipher.encrypt(pad(flag, 16))
print(f"{ct = }")