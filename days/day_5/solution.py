import os
from collections import deque


#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):

    """Converting lines to usable input"""
    
    crate_height = 0
    split_txt = txt.splitlines()
    for x in split_txt:
        if x[1] == "1":
            break
        crate_height += 1
    
    crate_list = [x for x in split_txt[crate_height].split() if x != ""]
    crate_list_ind_hash = {x:y for y,x in enumerate(split_txt[crate_height]) if x.isnumeric()}
    crate_dict = dict()
    
    for crate in crate_list:
        stack = deque()

        for x in split_txt[:crate_height]:

            crate_pos = crate_list_ind_hash[crate]
            if x[crate_pos].isalpha():
                stack.append(x[crate_pos])
        
        crate_dict[crate.strip()] = stack

    instructions = list()

    for move in split_txt[crate_height+2:]:

        qty, origin, destination = [x for x in move.split() if x.isnumeric()]
        moves = (int(qty), (origin, destination)) 
        instructions.append(moves)

    return (crate_dict, instructions)


def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------

def part_one():
    inp = get_input("input.txt")
    stacks, moves = inp

    for m in moves:

        for i in range(m[0]):
            crate = stacks[m[1][0]].popleft()
            stacks[m[1][1]].appendleft(crate)

    return [x[0] for x in stacks.values()]


def part_two():
    inp = get_input("input.txt")
    stacks, moves = inp

    for m in moves:

        tmp_deq = deque()
        for i in range(m[0]):
            crate = stacks[m[1][0]].popleft()
            tmp_deq.appendleft(crate)

        stacks[m[1][1]].extendleft(tmp_deq)
        
    return [x[0] for x in stacks.values()]

#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")