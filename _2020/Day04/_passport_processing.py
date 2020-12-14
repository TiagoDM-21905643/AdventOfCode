from _2020.help_functions import get_function_exec_time

DATA_LIST = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# cid not included

def check_passport_part1(passport_data):
    for data in DATA_LIST:
        if data not in passport_data:
            return False
    return True
def part1(file_name):
    file = open(file_name).readlines()
    passport_data = []
    count_valid_passports = 0
    for line in file:
        if line == '\n':
            if check_passport_part1(passport_data):
                count_valid_passports += 1
            passport_data.clear()
        else:
            line_data = line.split(" ")
            for data in line_data:
                passport_data.append(data.split(":")[0])
    return count_valid_passports

def check_is_number(data):
    for char in data:
        if not char.isdigit():
            return False
    return True
def check_byr(data):
    return len(data) == 4 and check_is_number(data) and 1920 <= int(data) <= 2002
def check_iyr(data):
    return len(data) == 4 and check_is_number(data) and 2010 <= int(data) <= 2020
def check_eyr(data):
    return len(data) == 4 and check_is_number(data) and 2020 <= int(data) <= 2030
def check_hgt(data):
    if len(data) < 3 or not check_is_number(data[:len(data) - 2]):
        return False
    num = int(data[:len(data) - 2])
    measure_unit = data[len(data) - 2:]
    if measure_unit == 'cm':
        return 150 <= num <= 193
    elif measure_unit == 'in':
        return 59 <= num <= 76
    else:
        return False
def check_hcl(data):
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f']
    if data[0] != '#':
        return False
    for i in range(1, len(data)):
        if not data[i].isdigit() and data[i] not in valid_letters:
            return False
    return True
def check_ecl(data):
    valid_data = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return data in valid_data
def check_pid(data):
    if len(data) != 9:
        return False
    return check_is_number(data)

def check_data(data_name, data):
    switcher = {
        'byr': check_byr(data),
        'iyr': check_iyr(data),
        'eyr': check_eyr(data),
        'hgt': check_hgt(data),
        'hcl': check_hcl(data),
        'ecl': check_ecl(data),
        'pid': check_pid(data),
        'cid': True
    }
    return switcher.get(data_name)
def check_passport_part2(passport_data):
    if not check_passport_part1(passport_data.keys()):
        return False
    for key in passport_data.keys():
        # print(key + " : " + passport_data[key].strip() + " -> " + str(check_data(key, passport_data[key].strip())))
        if not check_data(key, passport_data[key].strip()):
            return False
    return True
def part2(file_name):
    file = open(file_name).readlines()
    passport_data = {}
    count_valid_passports = 0
    for line in file:
        if line == '\n':
            if check_passport_part2(passport_data):
                count_valid_passports += 1
            passport_data.clear()
        else:
            line_data = line.split(" ")
            for data in line_data:
                data_name_and_info = data.split(":")
                passport_data[data_name_and_info[0]] = data_name_and_info[1]
    return count_valid_passports


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
