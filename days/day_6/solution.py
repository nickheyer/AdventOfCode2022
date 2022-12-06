import os
from collections import deque


#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):

    """Converting lines to usable input"""
    
    return txt.strip()


def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------

def part_one():
    inp = get_input("input.txt")
    
    four_char = deque()

    for i, char in enumerate(inp):
        four_char.append(char)
        
        if len(four_char) == 5:
            four_char.popleft()
        if len(set(four_char)) == 4:
            return i+1



def part_two():
    inp = get_input("input.txt")
    
    four_char = deque()

    for i, char in enumerate(inp):
        four_char.append(char)
        
        if len(four_char) == 15:
            four_char.popleft()
        if len(set(four_char)) == 14:
            return i+1

#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")