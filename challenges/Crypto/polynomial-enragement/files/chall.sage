from Crypto.Util.number import *

flag = b"SIVUSCG{REDACTED}"

P.<x> = PolynomialRing(ZZ)

flag_poly = list(flag)

f = 0
for i in range(len(flag_poly)):
	f += (x^i)*flag_poly[i]

g = P.random_element(degree=10)
h = P.random_element(degree=10)

noise1 = P.random_element(degree=5)
noise2 = P.random_element(degree=5)


poly1 = f*g + noise1
poly2 = f*h + noise2

print(poly1)
print(poly2)