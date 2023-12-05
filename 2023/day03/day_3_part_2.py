import re
import itertools
import math
import heapq
import bisect
import sys
import functools
from collections import OrderedDict, Counter
from typing import List

symbols = ['@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '/']
# to avoid recounting the same number from multiple symbol hits
hit_dict: dict[tuple, bool] = {}
# to track all nums
numbers_dict: dict[tuple, int] = {}
# to track all symbol positions of interest
symbols_pos_list = []

total_sum = 0
def get_full_num_and_mark_all_hits_from_pos(x, y):
    # move forward in positions and mark as hits until we pass the end of the value
    number_as_str = ""
    while True:
        #print(x, y)
        if (x, y) in numbers_dict and (x, y) not in hit_dict:
            (start_num_pos, cur_digit) = numbers_dict[(x, y)]
            number_as_str += str(cur_digit)
            hit_dict[(x, y)] = True
            x += 1
        else:
            if number_as_str == "":
                return 0
            else: return int(number_as_str)

def make_hits_around_position_and_get_gear_ratio(x, y, width, height) -> int:
    nums: List[int] = []
    for i in range(max(x - 1, 0), min(x + 2, width)):
        for j in range(max(y - 1, 0), min(y + 2, height)):
            # ignore the symbol
            if (i, j) != (x, y):
                # now check if its a number
                if (i, j) in numbers_dict:
                    (start_num_pos, cur_digit) = numbers_dict[(i, j)]
                    start_num_x, start_num_y = start_num_pos
                    # need to mark all digit positions of the number as hits, then return full value to add to the sum
                    full_number_value: int = get_full_num_and_mark_all_hits_from_pos(start_num_x, start_num_y)
                    if full_number_value != 0:
                        nums.append(full_number_value)
    if len(nums) == 2:
        return int(nums[0]) * int(nums[1])
    else: return 0

def do_it(file_path: str) -> {}:
    # define valid bounds
    width = 0
    height = 0
    with open(file_path, 'r') as file:
        lines: List[str] = file.read().split("\n")
        height = len(lines)

        for y, line in enumerate(lines):
            width = len(line)
            start_num_pos = ()
            for x, character in enumerate(line):
                if character.isdigit():
                    # update start num pos
                    if start_num_pos == ():
                        start_num_pos = (x, y)
                    # a valid number position in the dict just points to the start of the number
                    numbers_dict[(x, y)] = start_num_pos, int(character)
                else: start_num_pos = ()
                if character in symbols:
                    symbols_pos_list.append((x, y))
    total = 0
    # now check around every symbol
    for symbol_pos in symbols_pos_list:
        x, y = symbol_pos
        total += make_hits_around_position_and_get_gear_ratio(x, y, width, height)

    return total

print(f"TEST = {do_it('part_2_sample_input.txt')}")
print(f"REAL = {do_it('input.txt')}")