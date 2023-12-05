import re
import itertools
import math
import heapq
import bisect
import sys
import functools
from collections import OrderedDict, Counter
from typing import List

def do_it(file_path: str) -> {}:
    total = 0
    with open(file_path, 'r') as file:
        lines: List[str] = file.read().split("\n")

        for line in lines:
            data_parts = line.split(":")
            card_parts = data_parts[0].split(" ")
            this_card_number = card_parts[1]
            num_set_parts = data_parts[1].strip().split("|")
            winning_nums_sorted = num_set_parts[0].split(" ")
            my_nums_sorted = num_set_parts[1].split(" ")

            total_nums = winning_nums_sorted + my_nums_sorted
            counter = Counter(total_nums)
            del counter['']

            total_matches: int = 0
            for count in counter:
                total_matches += counter[count] - 1
            print(f"total matches = {total_matches}")

            if total_matches > 0:
                pts = 1
                for _ in range(1, total_matches):
                    pts *= 2
            else:
                pts = 0
            total += pts
    return total

print(f"TEST = {do_it('part_1_sample_input.txt')}")
#print(f"REAL = {do_it('input.txt')}")