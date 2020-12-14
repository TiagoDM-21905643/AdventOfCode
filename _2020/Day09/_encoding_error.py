from _2020.help_functions import get_function_exec_time

def check_impossible_sum(num, numbers):
    for number in numbers:
        if num - number in numbers:
            return False
    return True

def part1(file_name, preample):
    with open(file_name) as file:
        numbers = list(int(line) for line in file.readlines())
    for pos in range(0, len(numbers)):
        if pos >= preample and check_impossible_sum(numbers[pos], numbers[pos - preample:pos]):
            return numbers[pos]

def check_consecutive_sum(numbers, target_num):
    sum_ = 0
    for num in numbers:
        sum_ += num
        if sum_ > target_num:
            return False
        elif sum_ == target_num:
            return True
    return False

def get_largest_number(numbers, target_num):
    largest_num = 0
    sum_ = 0
    for num in numbers:
        sum_ += num
        if num > largest_num:
            largest_num = num
        if sum_ == target_num:
            break
    return largest_num

def part2(file_name, preample):
    with open(file_name) as file:
        numbers = list(int(line) for line in file.readlines())
    invalid_number = 0
    for pos in range(0, len(numbers)):
        if pos >= preample and check_impossible_sum(numbers[pos], numbers[pos-preample:pos]):
            invalid_number = numbers[pos]
    if invalid_number == 0:
        print('Invalid number not found')
    for pos in range(0, len(numbers)):
        numbers_to_check = numbers[pos:]
        if check_consecutive_sum(numbers_to_check, invalid_number):
            return numbers[pos] + get_largest_number(numbers_to_check, invalid_number)


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt", 5)
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt", 25)
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt", 5)
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt", 25)
