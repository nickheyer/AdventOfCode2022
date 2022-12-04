import os


#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):
    inp = txt.splitlines() #Grabbing input
    """Converting lines to usable input"""
    inp = [list(map(lambda x: tuple(int(n) for n in x.split("-")), line.split(","))) for line in inp]
    return inp

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------

def part_one():
    inp = get_input("input.txt")
    
    range_covered = 0

    """For elf-one and elf-two in each pair, convert to a range, then to a set so we can perform
    intersections. If the quantity of intersecting numbers is the same as either elf, range is covered"""
    for e_one, e_two in inp:
        e_one, e_two = set(range(e_one[0], e_one[1] + 1)), set(range(e_two[0], e_two[1] + 1))
        if len(e_one.intersection(e_two)) in [len(e_one), len(e_two)]:
            range_covered += 1

    return range_covered


def part_two():
    inp = get_input("input.txt")

    range_covered = 0

    """For elf-one and elf-two in each pair, convert to a range, then to a set so we can perform
    intersections. If the quantity of intersecting numbers is greater than zero, there are overlaps"""
    for e_one, e_two in inp:
        e_one, e_two = set(range(e_one[0], e_one[1] + 1)), set(range(e_two[0], e_two[1] + 1))
        if len(e_one.intersection(e_two)) > 0:
            range_covered += 1

    return range_covered

#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")