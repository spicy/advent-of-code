import re
import itertools
import math
import heapq
import bisect
import sys
import functools
from collections import OrderedDict, Counter, deque  # Import deque
from typing import List

def do_it(file_path: str) -> {}:
    total = 0
    with open(file_path, 'r') as file:
        lines: List[str] = file.read().split("\n")
        original_cards = []
        cards = deque()

        # first add all original cards..
        for card in lines:
            original_cards.append(card)
            cards.append(card)

        total_cards = 0
        # then run the card and create copies..
        while cards:
            total_cards += 1
            print(len(cards))
            card = cards.popleft()

            data_parts = card.split(":")
            number_str = data_parts[0].replace(' ', '').replace('Card', '')
            this_card_number = int(number_str)
            num_set_parts = data_parts[1].strip().split("|")
            winning_nums_sorted = num_set_parts[0].split(" ")
            my_nums = num_set_parts[1].split(" ")

            total_nums = winning_nums_sorted + my_nums
            counter = Counter(total_nums)
            del counter['']

            total_matches: int = 0
            for count in counter:
                total_matches += counter[count] - 1

            if total_matches > 0:
                for index in range(total_matches):
                    cards.append(original_cards[this_card_number + index])

    return total_cards

#print(f"TEST = {do_it('part_2_sample_input.txt')}")
print(f"REAL = {do_it('input.txt')}")