from fastapi import FastAPI
import zlib
import string
from secret import secret
from Crypto.Cipher import ChaCha20

app = FastAPI()

assert len(secret) == 32
assert secret.startswith("SIVUSCG{") and secret.endswith("}")
assert set(secret[8:-1]).issubset(string.ascii_letters + string.digits + '_')

@app.get("/sign_compress_encrypt")
def sign_compress_encrypt(data: str):
    signed = secret + data + secret
    compressed = zlib.compress(signed.encode())
    cipher = ChaCha20.new(key=secret.encode())
    encrypted = cipher.encrypt(compressed)
    return {"nonce": cipher.nonce.hex(), "ciphertext": encrypted.hex()}

