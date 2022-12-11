import os
from collections import deque

#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):
    """Converting lines to usable input"""
    inp = list()

    for line in txt.splitlines():
        if line == "noop":
            inp.append("noop")
        else:
            inp.append(int(line.split()[1]))
    
    return inp

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------

def part_one():
    inp = get_input("input.txt")
    x_value = 1

    signal_str = 0

    line_num = 0
    cycle_num = 1
    while (line_num < len(inp)):

        current = inp[line_num]
        if type(current) == str:
            if cycle_num in [20, 60, 100, 140, 180, 220]:
                    signal_str += cycle_num * x_value
                    print(f"Current X: {x_value}\nCurrent Cycle: {cycle_num}")
            cycle_num += 1
        else:

            end_cycle = cycle_num + 2
            while (cycle_num < end_cycle):

                if cycle_num in [20, 60, 100, 140, 180, 220]:
                    signal_str += cycle_num * x_value
                    print(f"Current X: {x_value}\nCurrent Cycle: {cycle_num}")
                
                cycle_num += 1
            x_value += current


        
        line_num += 1



    return signal_str



def part_two():
    inp = get_input("input.txt")
    x_value = 1

    crt = "\n#"

    cycle_num = 1

    def adv_cycle(cyc_num, crt_str):

        if cyc_num != 0 and cyc_num % 40 == 0:
            crt_str += "\n"
         
        if cyc_num % 40 in [x_value-1, x_value, x_value+1]:
            crt_str += "#"
        else:
            crt_str += "."
        

        cyc_num += 1

        return cyc_num, crt_str

    for line in inp:


        if type(line) == str: # "noop".
            cycle_num, crt = adv_cycle(cycle_num, crt)
        else:

            end_cycle = cycle_num + 2
            while (cycle_num < end_cycle):
                if cycle_num == end_cycle - 1:
                    x_value += line
                cycle_num, crt = adv_cycle(cycle_num, crt)

    return crt


#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")