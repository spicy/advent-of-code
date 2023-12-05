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
        sets: List[set] = []
        counter = 0

        for line in lines:
            counter += 1
            sets.append(set(line.replace('\n', '')))

            if counter == 3:
                common_characters = sets[0] & sets[1] & sets[2]
                sets.clear()
                counter = 0
                for common_char in common_characters:
                    total_sum += get_priority(common_char)
    print(total_sum)

#do_it('pt2_sample_input.txt')
#do_it('input.txt')