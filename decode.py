#!/usr/bin/env python3

import json
from base64 import b32decode

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

uwu_map = dict(zip(uwu_list, b32_chars))

ciphertext = open("encoded.txt").read().strip().split(" ")
encoded_plaintext = "".join(uwu_map[word] for word in ciphertext)

if len(encoded_plaintext) % 8 != 0:
    encoded_plaintext += "="*(8-len(encoded_plaintext)%8)

print(b32decode(encoded_plaintext))