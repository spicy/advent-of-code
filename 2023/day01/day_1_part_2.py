import re
from typing import List

num_string_to_int_map: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def try_get_number_str_match(input_str: str):
    regex_num_pattern = r"^(one|two|three|four|five|six|seven|eight|nine)"
    match = re.match(regex_num_pattern, input_str)
    if match:
        return match.group(0)
    return None

def sum_first_and_last(cur_list: List[int]) -> int:
    concatenated = f"{cur_list[0]}{cur_list[-1]}"
    return int(concatenated)

def do_it(file_path: str) -> int:
    running_list: List[int] = []
    running_sum: int = 0

    with open(file_path, 'r') as file:
        running_input = file.read()

        input_length = len(running_input)

        for i in range(input_length):
            try_num_match = try_get_number_str_match(running_input)
            if try_num_match in num_string_to_int_map:
                running_list.append(num_string_to_int_map[try_num_match])

            current_char = running_input[0]
            if current_char.isdigit():
                running_list.append(int(current_char))
            elif current_char == '\n' and running_list:
                running_sum += sum_first_and_last(running_list)
                running_list.clear()

            # remove the first character
            running_input = running_input[1:]

    if running_list:
        running_sum = sum_first_and_last(running_list, running_sum)

    return running_sum

running_sum = do_it('input.txt')
print(f"Final sum = {running_sum}")