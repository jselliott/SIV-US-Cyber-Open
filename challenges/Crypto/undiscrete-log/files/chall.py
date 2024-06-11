from Crypto.Util.number import bytes_to_long, isPrime
import random
from math import prod

print("-------------------")
print("Welcome to the flag giver where we give you flags on your own demands!")
print("Good luck on this one though. You'll need it")
print("-------------------")

flag = bytes_to_long(b"SIVUSCG{REDACTED}")

p = int(input("Give me a prime! Any Prime! Just make sure its safe though: "))
factors = list(map(int, input("Give me its factors (p-1): ").split()))
factors.sort()

assert isPrime(p), "Give me a prime next time!"
assert p.bit_length() == 512, "Too small of a prime!"
assert prod(factors) == p-1, "Can you factor lmao?"
assert factors[-1] > 2**400, "Give me a safer prime!"

g = random.randint(2,p)
ciph = pow(g,flag,p)

print(f"{g = }")
print(f"{ciph = }")