# 加密文件和文件夹

import sys
import os
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex


def encrypt_dir(path):
    for root, _, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path + " is encrypting.")
            encrypt_file(file_path)


def encrypt_file(path):
    # get the plaintext
    with open(path) as f:
        plain_text = f.read()

    # The key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes.
    key = b'this is a 16 key'

    iv = Random.new().read(AES.block_size)
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = iv + mycipher.encrypt(plain_text.encode())

    # output
    with open(path + ".bin", "wb") as file_out:
        file_out.write(ciphertext[16:])


path = input("请输入文件名:")
if os.path.isdir(path) and os.path.exists(path):
    encrypt_dir(path)
elif os.path.isfile(path) and os.path.exists(path):
    encrypt_file(path)
else:
    print("it's a special file(socket,FIFO,device file)")