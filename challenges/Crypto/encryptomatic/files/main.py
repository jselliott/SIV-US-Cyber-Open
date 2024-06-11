from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Random Key
key = os.urandom(16)
flag = os.getenv("FLAG","SIVUSCG{t3st_fl4g}")

cipher = AES.new(key, AES.MODE_ECB)

print("****************************************")
print("   Welcome to the USCG Encryptomatic!   ")
print("  Please enter your message to encrypt  ")
print("and I will add my flag for safe-keeping.")
print("****************************************")

while True:
    try:
        msg = input("> ")
        msg += flag

        ciphertext = cipher.encrypt(pad(msg.encode(),16))
        print("Encrypted: "+ciphertext.hex())
    except EOFError:
        pass