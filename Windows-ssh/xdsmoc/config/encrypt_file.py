# -*- coding: utf-8 -*-

import os
from Crypto.Cipher import AES
from Crypto.Util import Counter


class Aescrypt():
    def __init__(self, key):
        self.key = self.add_16(key)
        # self.model = AES.MODE_CBC

    def add_16(self, par):
        if type(par) == str:
            par = par.encode()
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesencrypt(self, text):
        try:
            text = self.add_16(text)
            self.aes = AES.new(self.key,AES.MODE_CTR, counter=Counter.new(128))
            self.encrypt_text = self.aes.encrypt(text)
            return self.encrypt_text
        except Exception as e:
            print(e)

    def aesdecrypt(self, text):
        self.aes = AES.new(self.key, AES.MODE_CTR, counter=Counter.new(128))
        self.decrypt_text = self.aes.decrypt(text)
        self.decrypt_text = self.decrypt_text.strip(b"\x00")
        return self.decrypt_text

    def encrypt_file(self, filepath, encrypt_filepath=''):
        # Load the data
        with open(filepath, 'rb') as f:
            data = f.read()
        # Encrypt the data
        data = self.aesencrypt(data)
        # The encrypted data is written to the encrypted file
        if not encrypt_filepath:
            filepath = os.path.split(filepath)
            encrypt_filepath = filepath[0] + '/encrypt_' + filepath[1]
        with open(encrypt_filepath, 'wb') as f:
            f.write(data)

    def decrypt_file(self, encrypt_filepath, decrypt_filepath=''):
        # Load the data
        with open(encrypt_filepath, 'rb') as f:
            data = f.read()
        # decrypt the data
        data = self.aesdecrypt(data)
        if not decrypt_filepath:
            encrypt_filepath = os.path.split(encrypt_filepath)
            decrypt_filepath = encrypt_filepath[0] + '/decrypt_' + encrypt_filepath[1]
        with open(decrypt_filepath, 'wb') as f:
            f.write(data)
