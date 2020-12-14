from _2020.help_functions import get_function_exec_time

def get_row(line):
    minimum = 0
    maximum = 127
    for char in line:
        # upper half
        if char == 'B':
            if maximum % 2 == 0:
                minimum += int((maximum - minimum) / 2)
            else:
                minimum += int((maximum - minimum) / 2) + 1
        # lower half
        elif char == 'F':
            if maximum % 2 == 0:
                maximum -= int((maximum - minimum) / 2)
            else:
                maximum -= int((maximum - minimum) / 2) + 1
    return minimum if line[6] == 'F' else maximum

def get_colum(line):
    minimum = 0
    maximum = 7
    for char in line:
        # upper half
        if char == 'R':
            if maximum % 2 == 0:
                minimum += int((maximum - minimum) / 2)
            else:
                minimum += int((maximum - minimum) / 2) + 1
        # lower half
        elif char == 'L':
            if maximum % 2 == 0:
                maximum -= int((maximum - minimum) / 2)
            else:
                maximum -= int((maximum - minimum) / 2) + 1
    return minimum if line[2] == 'L' else maximum

def part1(file_name):
    file = open(file_name).readlines()
    max_seat_id = 0
    for line in file:
        row = get_row(line[:7].strip())
        column = get_colum(line[7:].strip())
        seat_id = row * 8 + column
        # print('row ' + str(row) + ', column ' + str(column) + ', seat id ' + str(seat_id))
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def get_seat_id_list():
    seat_id_list = []
    for i in range(0, 128):
        for j in range(0, 8):
            seat_id_list.append(i * 8 + j)
    return seat_id_list

def part2(file_name):
    seat_id_list = get_seat_id_list()
    file = open(file_name).readlines()
    for line in file:
        row = get_row(line[:7].strip())
        column = get_colum(line[7:].strip())
        seat_id = row * 8 + column
        # print('row ' + str(row) + ', column ' + str(column) + ', seat id ' + str(seat_id))
        if seat_id in seat_id_list:
            seat_id_list.remove(seat_id)
    # print(seat_id_list)
    for i in range(0, len(seat_id_list) - 1):
        if seat_id_list[i] + 1 != seat_id_list[i + 1]:
            return seat_id_list[i + 1]
    return 0


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
