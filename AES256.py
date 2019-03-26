# AES 256 encryption/decryption using pycrypto library

import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

class aes(object):
    """docstring for aes"""
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode("utf-8")).digest()
        self.BLOCK_SIZE = 16
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[lambdaen(s) - 1:])]

    # password = input("Enter encryption password: ")


    def encrypt(self,raw):
       
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))


    def decrypt(self,enc, password):
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))


# First let us encrypt secret message
# encrypted = encrypt("This is a secret message", password)
# print(encrypted)

# # Let us decrypt using our original password
# decrypted = decrypt(encrypted, password)
# print(bytes.decode(decrypted))