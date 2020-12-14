from _2020.help_functions import get_function_exec_time

def count_letter_occurrences(letter, password):
    count = 0
    for pass_letter in password:
        if pass_letter == letter:
            count += 1
    return count

def part1(file_name):
    file = open(file_name).readlines()
    count_valid_lines = 0
    for line in file:
        rule_and_pass = line.split(": ")
        range_and_letter = rule_and_pass[0].split(" ")
        min_and_max = range_and_letter[0].split("-")
        letter = range_and_letter[1][0]
        password = rule_and_pass[1]
        minimum = int(min_and_max[0])
        maximum = int(min_and_max[1])
        count = count_letter_occurrences(letter, password)
        if minimum <= count <= maximum:
            count_valid_lines += 1
    return count_valid_lines


def part2(file_name):
    file = open(file_name).readlines()
    count_valid_lines = 0
    for line in file:
        rule_and_pass = line.split(":")
        range_and_letter = rule_and_pass[0].split(" ")
        min_and_max = range_and_letter[0].split("-")
        letter = range_and_letter[1][0]
        password = rule_and_pass[1]
        pos1 = int(min_and_max[0])
        pos2 = int(min_and_max[1])
        if pos1 < len(password) and pos2 < len(password) and \
                ((password[pos1] == letter) ^ (password[pos2] == letter)):
            count_valid_lines += 1
    return count_valid_lines


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
