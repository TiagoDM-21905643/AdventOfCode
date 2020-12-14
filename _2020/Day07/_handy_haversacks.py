from _2020.help_functions import get_function_exec_time

class Bag:
    def __init__(self, type, color, quantity):
        self.type = type
        self.color = color
        self.quantity = quantity
        self.bags_that_can_hold = set()

    def get_quantity(self):
        return self.quantity

    def get_bags_that_can_hold(self):
        return self.bags_that_can_hold

    def add_to_bags_can_hold(self, bag):
        self.bags_that_can_hold.add(bag)

    def can_contain(self, bag_name):
        for bag in self.bags_that_can_hold:
            if bag_name == str(bag):
                return True
        return False

    def get_info(self):
        return str(self.quantity) + ' ' + self.type + ' ' + self.color + ' -> {' + \
               ', '.join(str(bag.get_info()) for bag in self.bags_that_can_hold) + '}'

    def __str__(self):
        return self.type + ' ' + self.color

def print_rules(rules):
    for rule in rules.values():
        print(rule.get_info())

def get_rules(file):
    rules = {}
    for line in file:
        parent_names = line.split('contain ')[0].split(' ')
        containable_bags = line.split('contain ')[1].split(', ')
        parent = Bag(parent_names[0], parent_names[1], 0)
        for containable_bag in containable_bags:
            split_info = containable_bag.split(' ')
            if split_info[0] != 'no':
                num = int(split_info[0])
                bag = Bag(split_info[1], split_info[2], num)
                parent.add_to_bags_can_hold(bag)
        rules[str(parent)] = parent
    return rules

def get_bags_that_can_hold(bag_name, rules):
    bags_that_can_contain = set()
    parent_bags_to_check = set()
    for bag in rules.values():
        if bag.can_contain(bag_name):
            bags_that_can_contain.add(str(bag))
            if str(bag) not in parent_bags_to_check:
                parent_bags_to_check.add(str(bag))
    if parent_bags_to_check:
        for bag_name_ in parent_bags_to_check:
            for bag_ in get_bags_that_can_hold(bag_name_, rules):
                bags_that_can_contain.add(bag_)
    return bags_that_can_contain

def part1(file_name):
    file = open(file_name).readlines()
    rules = get_rules(file)
    return len(get_bags_that_can_hold('shiny gold', rules))

def get_bags_that_can_contain(bag_name, rules):
    parent_bag = rules[bag_name]
    bag_map = {}
    for bag in parent_bag.get_bags_that_can_hold():
        bag_map[str(bag)] = bag.get_quantity()
    return bag_map

def count_bags_that_can_contain(bag_name, rules):
    count = 0
    bag_map = get_bags_that_can_contain(bag_name, rules)
    for bag_name_ in bag_map.keys():
        num = bag_map[bag_name_]
        count += num + num * count_bags_that_can_contain(bag_name_, rules)
    return count

def part2(file_name):
    file = open(file_name).readlines()
    rules = get_rules(file)
    return count_bags_that_can_contain('shiny gold', rules)


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (example_input2) -> ", part2, "example_input2.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")
