from _2020.help_functions import get_function_exec_time

def part1(file_name):
    file = open(file_name).readlines()
    for line in file:
        num1 = int(line)
        num2 = 2020 - num1
        if str(num2) + '\n' in file:
            return num1 * num2
    return 0


def part2(file_name):
    file = open(file_name).readlines()
    for i in range(0, len(file)):
        for j in range(i + 1, len(file)):
            num1 = int(file[i])
            num2 = int(file[j])
            num3 = 2020 - num1 - num2
            if str(num3) + '\n' in file:
                return num1 * num2 * num3
    return 0


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
