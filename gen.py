#!/usr/bin/env python3

import json
import random

sample_size = 32
uwu_list = json.load(open("dictionary.json"))

if len(uwu_list["words"]) > sample_size / 2.2:
    print("Using random combined selection") 
    uwu_list = uwu_list["faces"] + uwu_list["words"]

else:
    print("Using words heavy random selection")
    uwu_list = uwu_list["words"] + random.sample(uwu_list["faces"], sample_size - len(uwu_list["words"]) + int(sample_size / 4))
    print(len(uwu_list))

uwu_map = {}

uwu_map["map"] = random.sample(uwu_list, sample_size)

json.dump(uwu_map, open("map.json", "w"), indent=4)