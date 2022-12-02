import sys
import os

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return fp.read()

def part_one():
    inp = get_input("input.txt").splitlines()
    sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    inp = list(map(lambda x: int(x) if x != "" else -1, inp))
    


    largest_elf = current_elf = 0
    
    for cal in inp:
        if cal == -1:
            largest_elf = max(largest_elf, current_elf)
            current_elf = 0
            continue
        current_elf += cal
        



    
    return largest_elf





def part_two():
    inp = get_input("input.txt").splitlines()
    sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

""".splitlines()

    inp = list(map(lambda x: int(x) if x != "" else -1, inp))
    


    largest_elves = list() 
    current_elf = 0
    
    for cal in inp:
        if cal == -1:

            if len(largest_elves) < 3:
                largest_elves.append(current_elf)
            else:

                largest_elves.sort(reverse=True)
                

                for x in range(3):
                    if current_elf > largest_elves[x]:
                        largest_elves.insert(x, current_elf)
                        largest_elves.pop(-1)
                        print(largest_elves)
                        break

                

            current_elf = 0
            continue
        current_elf += cal
        



    
    return sum(largest_elves)





print(part_two())