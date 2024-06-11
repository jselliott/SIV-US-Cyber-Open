from Crypto.Util.number import *
from math import gcd
import random

P = getPrime(512)
Q = getPrime(512)
N = P*Q

e = 3
assert gcd(e, (P-1)*(Q-1)) == 1

flag = bytes_to_long(b"SIVUSCG{REDACTED}")

class LCG:
	def __init__(self, a, b, p, seed):
		self.a = a
		self.b = b
		self.p = p
		self.seed = seed

	def next(self):
		self.seed = (self.a*self.seed + self.b) % self.p
		return self.seed


p = getPrime(128)
a = random.randint(0, 2**32)
b = random.randint(0, 2**32)
seed = random.randint(0, p)
lcg = LCG(a,b,p, seed)

outputs = []
for i in range(6):
	outputs.append(lcg.next())

hints = []
for i in range(3):
	hints.append(lcg.next())

c1 = pow(outputs[0] * flag + outputs[1], e, N)
c2 = pow(outputs[2] * flag + outputs[3], e, N)
c3 = pow(outputs[4] * flag + outputs[5], e, N)

print(f"{p = }")
print(f"{N = }")
print(f"{c1 = }")
print(f"{c2 = }")
print(f"{c3 = }")
print(f"{hints = }")



print(outputs)