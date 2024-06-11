from Crypto.Util.number import bytes_to_long, getPrime
from secret import FLAG

def genRSA():
  e = 3
  while True:
    p = getPrime(512)
    q = getPrime(512)
    phi = (p-1)*(q-1)
    if phi % e:break
  n = p*q
  d = pow(e,-1,phi)
  return (e,n,d)
  
def main():
  e,n,d = genRSA()
  enc_flag = pow(bytes_to_long(FLAG),e,n)
  print("Here is your encrypted flag: " + str(enc_flag))
  print("Here is your public key:")
  print("n: " + str(n))
  print("e: " + str(e))

if __name__ == '__main__': main()