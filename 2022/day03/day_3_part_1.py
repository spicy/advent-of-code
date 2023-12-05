import re
import itertools
import math
import heapq
import bisect
import sys
import functools
from collections import OrderedDict, Counter
from typing import List
# ASCII a-z (97-122)
# ASCII A-Z (65-90)
def get_priority(character: chr):
    if character.islower():
       return ord(character) - 96
    else:
       return ord(character) - 38

def do_it(file_path: str) -> {}:
    total_sum = 0
    with open(file_path, 'r') as file:
        lines: List[str] = file.readlines()
        for line in lines:
            count = (len(line) - 1)
            half = int(count / 2)
            left_comp = line[0:half]
            right_comp = line[half:count]
            # find chars that appear in both comp strings, case sensitive
            left_set = set(left_comp)
            right_set = set(right_comp)
            common_characters = left_set.intersection(right_set)
            for common_char in common_characters:
                total_sum += get_priority(common_char)
    return total_sum

print(f"TEST = {do_it('pt1_sample_input.txt')}")
print(f"REAL = {do_it('input.txt')}")