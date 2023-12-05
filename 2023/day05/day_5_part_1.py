import re
import itertools
import math
import heapq
import bisect
import sys
import functools
from collections import OrderedDict, Counter
from typing import List, Tuple

seeds = []
map_order_dict = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
}

def get_num_from_seed_mapping(seed: int, map_order_dict: dict) -> int:
    num = seed
    for mapping in map_order_dict.values():
        for destination_start, source_start, range_length in mapping:
            # check if seed number is in range
            if source_start <= num < source_start + range_length:
                offset = num - source_start
                print(f"{num} - {source_start} = {offset}")
                num = destination_start + offset
                print(f"{destination_start} + {offset} = {num}")
                break
    return num

def do_it(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")
        seed_group_str = lines[0].split(":")[1].strip()
        seeds = [int(seed) for seed in seed_group_str.split()]
        del lines[0]
        lines = [line for line in lines if line]
        map_to_use_index = -1
        for line in lines:
            if "map" in line:
                map_to_use_index += 1
                continue
            destination_start, source_start, range_length = map(int, line.split())
            print(f"e e e = {destination_start, source_start, range_length}")
            map_order_dict[map_to_use_index].append((destination_start, source_start, range_length))

    location_numbers = []
    for seed in seeds:
        num = get_num_from_seed_mapping(seed, map_order_dict)
        location_numbers.append(num)
    return min(location_numbers)

print(f"TEST = {do_it('part_1_sample_input.txt')}")
#print(f"REAL = {do_it('input.txt')}")