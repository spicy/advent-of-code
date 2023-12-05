from typing import List

def add_to_sum(cur_list: List[int], cur_sum: int) -> int:
    concatenated = f"{cur_list[0]}{cur_list[-1]}"
    addition = int(concatenated)
    cur_sum += addition
    print(f"Added {addition} to runningSum. RunningSum = {cur_sum}")
    return cur_sum

def do_it(file_path: str) -> int:
    running_list: List[int] = []
    running_sum: int = 0

    with open(file_path, 'r') as file:
        for ch in file.read():
            if ch.isdigit():
                running_list.append(int(ch))
                print(running_list)
            elif ch == '\n' and running_list:
                running_sum = add_to_sum(running_list, running_sum)
                running_list.clear()

    if running_list:
        running_sum = add_to_sum(running_list, running_sum)

    return running_sum

running_sum = do_it('input.txt')
print(f"Final sum = {running_sum}")