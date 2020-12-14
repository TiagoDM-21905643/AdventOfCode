from _2020.help_functions import get_function_exec_time

class Instruction:
    def __init__(self, command, num):
        self.command = command
        self.num = num
        self.done = False

    def exec(self):
        self.done = True

    def reset(self):
        self.done = False

    def toggle_jmp_nop(self):
        self.command = 'nop' if self.command == 'jmp' else 'jmp'

def part1(file_name):
    with open(file_name) as file:
        instructions = list(Instruction(line.split(' ')[0], int(line.split(' ')[1])) for line in file.readlines())

    acc = 0
    pos = 0
    while True:
        instruction = instructions[pos]
        if instruction.done:
            return acc
        elif instruction.command == 'acc':
            acc += instruction.num
            instruction.exec()
        elif instruction.command == 'jmp':
            pos += instruction.num - 1
            instruction.exec()
        pos += 1

def part2(file_name):
    with open(file_name) as file:
        instructions = list(Instruction(line.split(' ')[0], int(line.split(' ')[1])) for line in file.readlines())

    for instruction_to_check in instructions:
        acc = 0
        pos = 0
        if instruction_to_check.command == 'nop' or instruction_to_check.command == 'jmp':
            instruction_to_check.toggle_jmp_nop()
            while True:
                instruction = instructions[pos]
                if instruction.done:
                    break
                elif instruction.command == 'acc':
                    acc += instruction.num
                    instruction.exec()
                elif instruction.command == 'jmp':
                    pos += instruction.num - 1
                    instruction.exec()
                if pos == len(instructions) - 1:
                    return acc
                pos += 1
            instruction_to_check.toggle_jmp_nop()
            for instruction in instructions:
                instruction.reset()


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
