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
        full_list = []
        bad_games = {}
        power_sum = 0

        # make each game
        for game_index, game in enumerate(games_list):
            game_data = []

            game_parts = game.split(":")
            print(f"game_parts = {game_parts}")

            cube_sets = game_parts[1].split(";")
            highest_red_num_in_all_sets = 0
            highest_blue_num_in_all_sets = 0
            highest_green_num_in_all_sets = 0

            # make each cube set
            for cube_set in cube_sets:
                cubes = []

                # split cube set into individual cubes
                cube_data = cube_set.split(",")

                # make each cube (has num then color)
                for cube in cube_data:
                    cube = cube.strip() #start/end spaces

                    matched_num = int(try_get_number_match(cube))
                    matched_color = try_get_color_match(cube)

                    if matched_color == "red":
                        if matched_num > highest_red_num_in_all_sets:
                            highest_red_num_in_all_sets = matched_num
                    if matched_color == "green":
                        if matched_num > highest_green_num_in_all_sets:
                            highest_green_num_in_all_sets = matched_num
                    if matched_color == "blue":
                        if matched_num > highest_blue_num_in_all_sets:
                            highest_blue_num_in_all_sets = matched_num

                    if matched_color in color_max_map.keys():
                        if int(matched_num) > color_max_map[matched_color]:
                            # we found a bad game, so add it...
                            bad_games[game_index + 1] = game_index + 1
                            print(f"game_index {game_index + 1} is bad because there is {matched_num} {matched_color} and the max for {matched_color} is {color_max_map[matched_color]}")
                    cubes.append(cube)
                game_data.append(cubes)
            full_list.append(game_data)

            power = highest_red_num_in_all_sets * highest_green_num_in_all_sets * highest_blue_num_in_all_sets
            power_sum += power
            print(f"power = {power}...... red = {highest_red_num_in_all_sets} * green = {highest_green_num_in_all_sets} * blue = {highest_blue_num_in_all_sets} *")

        return power_sum

power_sum = do_it('input.txt')

print(f"Final sum = {power_sum}")


########### TESTING ###########
test_input_file_path = 'p1_test_input.txt'

expected_test_output = 2286
actual_test_output = calculate_good_game_sum(do_it(test_input_file_path))
if actual_test_output != expected_test_output:
    print(f"********* TEST SUCCEEDED FOR {test_input_file_path} *********")
else:
    print(f"********* TEST FAILED FOR {test_input_file_path} *********\n TEST OUTPUT = {actual_test_output} and EXPECTED_OUTPUT = {expected_test_output}")


########### REAL OUTPUT ###########
real_input_file_path = 'final_input.txt'
real_output = calculate_good_game_sum(do_it(real_input_file_path))
print(f"********* REAL OUTPUT FOR PART ONE *********\n real_output = {real_output}")