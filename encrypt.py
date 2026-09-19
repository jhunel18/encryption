import os, hashlib
from cryptography.hazmat.primitives.ciphers \
     import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

val= input("Enter a string: ")
data = val.encode("utf-8")

key, iv = os.urandom(32), os.urandom(16)  # 256-bit

pad = padding.PKCS7(128).padder()
pt  = pad.update(data) + pad.finalize()
enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
ct  = enc.update(pt) + enc.finalize()

dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
unp = padding.PKCS7(128).unpadder()
raw = dec.update(ct) + dec.finalize()
back = unp.update(raw) + unp.finalize()

print('Match:', back == data)
print(hashlib.sha256(data).hexdigest())
print(hashlib.sha256(back).hexdigest())
