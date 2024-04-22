#!/usr/bin/env python3

import json

uwu_list = json.load(open("dictionary.json"))
uwu_list = uwu_list["faces"] + uwu_list["words"]

def find_unique(non_unique):
    seen = set()
    duplicate = []

    for i in non_unique:
        if i not in seen:
            seen.add(i)
            continue

        duplicate.append(i)
    print(duplicate)
        
print(f"Have {len(uwu_list)} words")

if len(uwu_list) != len(set(uwu_list)):
    print("Non unique list given")
    find_unique(uwu_list)
    exit()
