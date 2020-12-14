from _2020.help_functions import get_function_exec_time

def part1(file_name):
    file = open(file_name).readlines()
    count_per_question = {}
    team_yes_votes = set()
    for line in file:
        if line == '\n':
            for char in team_yes_votes:
                count_per_question[char] = count_per_question[char] + 1 if char in count_per_question else 1
            team_yes_votes.clear()
        else:
            for char in line.strip():
                team_yes_votes.add(char)
    answer = 0
    for value in count_per_question.values():
        answer += value
    return answer

def get_person_yes_votes(line):
    person_count_yes_votes = set()
    for char in line.strip():
        person_count_yes_votes.add(char)
    return person_count_yes_votes

def part2(file_name):
    file = open(file_name).readlines()
    count_per_question = {}
    team_yes_votes = set()
    people_yes_votes_list = []
    for line in file:
        if line == '\n':
            team_yes_votes = people_yes_votes_list[0]
            for people_yes_votes in people_yes_votes_list:
                team_yes_votes = team_yes_votes & people_yes_votes
            for char in team_yes_votes:
                count_per_question[char] = count_per_question[char] + 1 if char in count_per_question else 1
            team_yes_votes.clear()
            people_yes_votes_list.clear()
        else:
            people_yes_votes_list.append(get_person_yes_votes(line))
    answer = 0
    for value in count_per_question.values():
        answer += value
    return answer


get_function_exec_time("Part 1 (example_input) -> ", part1, "example_input.txt")
get_function_exec_time("Part 1 (final_input) -> ", part1, "final_input.txt")
get_function_exec_time("Part 2 (example_input) -> ", part2, "example_input.txt")
get_function_exec_time("Part 2 (final_input) -> ", part2, "final_input.txt")


# Resolucao de um deus
with open('final_input.txt') as f:
    data = f.read().strip()
print(sum(len(set(g.replace('\n', ''))) for g in data.split('\n\n')))
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in data.split('\n\n')))
