import re

color_max_map: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def try_get_color_match(input_str: str):
    regex_pattern = r"(red|green|blue)$"
    match = re.search(regex_pattern, input_str)
    if match:
        return match.group(1)
    return None

def try_get_number_match(input_str: str):
    regex_pattern = r"^[-+]?[0-9]+"
    match = re.match(regex_pattern, input_str)
    if match:
        return match.group(0)
    return None

def do_it(file_path: str) -> {}:
    with open(file_path, 'r') as file:
        original_input = file.read().replace(' ', '')
        games_list = original_input.split("\n")
        bad_games = {}

        # make each game
        for game_index, game in enumerate(games_list):
            game_parts = game.split(":")
            cube_sets = game_parts[1].split(";")

            # make each cube set
            for cube_set in cube_sets:

                # split cube set into individual cubes
                cube_data = cube_set.split(",")

                # make each cube (has num then color)
                for cube in cube_data:
                    cube = cube.strip()
                    matched_num = try_get_number_match(cube)
                    matched_color = try_get_color_match(cube)
                    if matched_color in color_max_map.keys():
                        if int(matched_num) > color_max_map[matched_color]:
                            bad_games[game_index + 1] = game_index + 1
                            print(f"game_index {game_index + 1} is bad because there is {matched_num} {matched_color} and the max for {matched_color} is {color_max_map[matched_color]}")
        return bad_games

def calculate_good_game_sum(bad_games):
    total_sum = 0
    for game_number in range(1, 101):
        if game_number not in bad_games:
            total_sum += game_number
    return total_sum

########### TESTING ###########
test_input_file_path = 'p1_test_input.txt'

expected_test_output = 8
actual_test_output = calculate_good_game_sum(do_it(test_input_file_path))
if actual_test_output != expected_test_output:
    print(f"********* TEST SUCCEEDED FOR {test_input_file_path} *********")
else:
    print(f"********* TEST FAILED FOR {test_input_file_path} *********\n TEST OUTPUT = {actual_test_output} and EXPECTED_OUTPUT = {expected_test_output}")


########### REAL OUTPUT ###########
real_input_file_path = 'final_input.txt'
real_output = calculate_good_game_sum(do_it(real_input_file_path))
print(f"********* REAL OUTPUT FOR PART ONE *********\n real_output = {real_output}")