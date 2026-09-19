from cryptography.hazmat.primitives.ciphers \
     import Cipher, algorithms, modes
raw = open('penguin.bmp','rb').read()
header, body = raw[:54], raw[54:]     # 54-byte header
key, iv = b'0'*32, b'0'*16
pad = (16 - len(body) % 16) % 16
body_p = body + b'\x00'*pad

def enc(mode):
    e = Cipher(algorithms.AES(key), mode).encryptor()
    return (e.update(body_p)+e.finalize())[:len(body)]

open('penguin_ecb.bmp','wb').write(header + enc(modes.ECB()))
open('penguin_cbc.bmp','wb').write(header + enc(modes.CBC(iv)))
