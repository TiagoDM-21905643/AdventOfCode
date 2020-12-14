from _2020.help_functions import get_function_exec_time

def count_trees(file, x_dist, y_dist):
    trees = 0
    pos = 0
    for i in range(0, len(file), y_dist):
        if file[i][pos] == '#':
            trees += 1
        if x_dist + pos >= len(file[i]) - 1:
            pos = x_dist - len(file[i]) + 1 + pos
        else:
            pos += x_dist
    return trees

def part1(file_name):
    file = open(file_name).readlines()
    return count_trees(file, 3, 1)

def part2(file_name):
    file = open(file_name).readlines()
    result = count_trees(file, 1, 1)
    result *= count_trees(file, 3, 1)
    result *= count_trees(file, 5, 1)
    result *= count_trees(file, 7, 1)
    result *= count_trees(file, 1, 2)
    return result


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
