import os
import string
from collections import defaultdict

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return fp.read()

def part_one():
    inp = get_input("input.txt").splitlines() #Grabbing input

    """Creating a key/value for each badge and it's associated priority"""
    atlas = string.ascii_lowercase + string.ascii_uppercase
    atlas = {v:i for i,v in enumerate([badge for badge in atlas], start=1)}

    priority_sum = 0

    """Splitting each rucksack into it's two compartments, evenly divided in half"""
    comps = [[set(x[:int(len(x)/2)]), set(x[int(len(x)/2):])] for x in inp]

    """For the first and second compartment, and for each item in the first compartment,
    check to see if any item is also in the second compartment. Each compartment has been
    converted to a set, so there won't be any duplicates."""
    for comp_one, comp_two in comps:
        for item in comp_one:
            if item in comp_two:
                priority_sum += atlas[item] #Adding to priority sum if common badge exists

    return priority_sum


def part_two():
    inp = get_input("input.txt").splitlines()
    
    """Converting each 'elf' into a set, to avoid duplicates"""
    inp = [set(x) for x in inp]
    
    atlas = string.ascii_lowercase + string.ascii_uppercase
    atlas = {v:i for i,v in enumerate([badge for badge in atlas], start=1)}

    priority_sum = 0

    """Splitting input into groups of 3 elves"""
    groups = list(zip(*(iter(inp),) * 3))


    """Finding common badge among all 3 elves per group"""
    for group in groups:
        badge_hash = defaultdict(lambda: 0)
        for elf in group:
            for badge in elf:
                if badge_hash[badge] == 2:
                    priority_sum += atlas[badge]
                else:
                    badge_hash[badge] += 1
    
    return priority_sum


print(part_two())