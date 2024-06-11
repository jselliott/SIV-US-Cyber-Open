from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from os import urandom
from secret import flag

def main():
  iv = urandom(16)
  key = b'SecretKey1234567'
  msg = b'Here is the flag for you: ' + flag
  cipher = AES.new(key, AES.MODE_CBC, iv)
  enc = cipher.encrypt(pad(msg,16))
  print("Key: " + key.decode())
  print("Encoded Flag: " + enc.hex())

if __name__ == '__main__': main()
