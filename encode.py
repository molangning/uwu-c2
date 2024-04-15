#!/usr/bin/env python3

import json
from base64 import b32encode

b32_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567")
uwu_list = json.load(open("map.json"))["map"]
unique_uwu_list = list(dict.fromkeys(uwu_list))

if uwu_list != unique_uwu_list:
    print("Non unique list given")
    print(uwu_list)
    print(unique_uwu_list)
    exit()

if len(unique_uwu_list) != 32:
    print(f"Uwu list is not of length 32 (Got {len(unique_uwu_list)})")
    exit()

uwu_map = dict(zip(b32_chars, uwu_list))

#plaintext = input("Enter your plaintext: ").encode()
plaintext = "This is a sample plaintext".encode()
encoded_text = b32encode(plaintext).strip(b"=").decode()
ciphertext = " ".join([uwu_map[char] for char in encoded_text])

print(ciphertext)
open("encoded.txt", "w").write(ciphertext)