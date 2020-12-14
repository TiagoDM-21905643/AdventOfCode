from _2020.help_functions import get_function_exec_time

def part1(file_name, preample):
    with open(file_name) as file:
        numbers = list(int(line) for line in file.readlines())

def part2(file_name, preample):
    with open(file_name) as file:
        numbers = list(int(line) for line in file.readlines())


print("Part 1 (example_input) -> " + str(part1("example_input.txt", 5)))
print("Part 1 (final_input) -> " + str(part1("final_input.txt", 25)))
print("Part 2 (example_input) -> " + str(part2("example_input.txt", 5)))
print("Part 2 (final_input) -> " + str(part2("final_input.txt", 25)))
