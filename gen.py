#!/usr/bin/env python3

import json
import random

uwu_list = json.load(open("dictionary.json"))
uwu_list = uwu_list["faces"] + uwu_list["words"]

uwu_map = {}
sample_size = 32

uwu_map["map"] = random.sample(uwu_list, sample_size)

json.dump(uwu_map, open("map.json", "w"), indent=4)