from Crypto.Util.number import *
import os
import random
import hashlib
from pwn import *
from functools import reduce
from secret import flag

def intxor(a,b):
    return a ^ b

def shuffle(x):
    n=len(x)
    assert(n < 256)
    for i in range(n-1):
        j = (bytes_to_long(os.urandom(1)) % (n-i)) + i
        tmp = x[i]
        x[i] = x[j]
        x[j] = tmp
    return x

def lfsr_gen():
    #Adapted from https://github.com/mkazmier/linear-register
    regs=[bytes_to_long(os.urandom(1)) & 1 for _ in range(128)]
    taps=[128] + list(set([bytes_to_long(os.urandom(1)) % 128 for _ in range(3)]))
    taps.sort()
    taps=taps[::-1]
    while True:
        output = 0
        for _ in range(64):
            output *= 2
            new_bit = reduce(intxor, [regs[(len(regs)-1)-t] for t in taps])
            del regs[0]
            regs.append(new_bit)
            output += new_bit
        yield output

def lcg_gen():
    m = getPrime(64)
    a = bytes_to_long(os.urandom(8))
    b = bytes_to_long(os.urandom(8))
    while (a >= m):
        a = bytes_to_long(os.urandom(8))
    state = bytes_to_long(os.urandom(8))
    while True:
        state = (a*state + b) % m
        yield state

def _xs64(state):
    mask=0xffffffffffffffff
    state = state & mask
    state ^= (state << 7) & mask
    state ^= (state >> 9) & mask
    return state & mask

def mt_gen():
    random.seed(bytes_to_long(os.urandom(8)))
    while True:
        top = random.getrandbits(32)
        bot = random.getrandbits(32)
        yield top << 32 | bot

def xs64_gen():
    state = bytes_to_long(os.urandom(8))
    while True:
        state = _xs64(state)
        yield state

def initialize():
    xs64g = xs64_gen()
    mtg = mt_gen()
    lcgg = lcg_gen()
    lfsrg = lfsr_gen()
    return xs64g, mtg, lcgg, lfsrg

xs64g, mtg, lcgg, lfsrg = initialize()

N=500

xs64 = [xs64g.next() for _ in range(N+1)]
mt = [mtg.next() for _ in range(N+1)]
lcg = [lcgg.next() for _ in range(N+1)]
lfsr = [lfsrg.next() for _ in range(N+1)]

raw_in = [xs64, mt, lcg, lfsr]

dist_out = []
for i in range(N):
    tmp = shuffle([raw_in[j][i] for j in range(len(raw_in))])
    dist_out.append(map(str,tmp))

tmp = [raw_in[j][N] for j in range(len(raw_in))]
key = "".join([long_to_bytes(x) for x in tmp])
print(xor(flag, hashlib.sha256(key).digest()).encode('hex'))
print(dist_out)