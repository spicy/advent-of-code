import os
import requests
from secret_session import SESSION

def make_puzzle_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}"

def fetch_puzzle_input(puzzle_url):
    input_url = f"{puzzle_url}/input"
    headers = {"Cookie": f"session={SESSION}"}
    response = requests.get(input_url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch puzzle input. Status code: {response.status_code}")

def write_puzzle_input(dirname, input_text):
    os.makedirs(dirname, exist_ok=True)
    with open(os.path.join(dirname, "input.txt"), "w") as input_file:
        input_file.write(input_text)
    with open(os.path.join(dirname, "part_1_sample_input.txt"), "w"):
        pass
    with open(os.path.join(dirname, "part_2_sample_input.txt"), "w"):
        pass

year = "2023"
day = "3"
puzzle_url = make_puzzle_url(year, day)
input_text = fetch_puzzle_input(puzzle_url)
write_puzzle_input("2023/day03", input_text)