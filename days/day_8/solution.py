import os


#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):
    """Converting lines to usable input"""
    inp = list()
    for line in txt.splitlines():
        line = list(map(lambda x: int(x), line))
        inp.append(line)
    return inp

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------

def part_one():
    inp = get_input("input.txt")

    count = 0

    for i, line in enumerate(inp):
        for j, tree in enumerate(line):

            sliced_arr = [x[j] for x in inp]
            #Checking left
            if j == 0 or tree > max(line[:j]):
                count += 1
            #Checking right
            elif j == len(line) - 1 or tree > max(line[j+1:]):
                count += 1
            #Checking up
            elif i == 0 or tree > max(sliced_arr[:i]):
                count += 1
            #Checking down
            elif i == len(sliced_arr) - 1 or tree > max(sliced_arr[i+1:]):
                count += 1

    return count


def part_two():
    inp = get_input("input.txt")

    score = 0

    for i, line in enumerate(inp):
        #Check left and right with double pointer method
        for j, tree in enumerate(line):

            l = r = u = d = 0

            sliced_arr = [x[j] for x in inp]

            if i not in [0, len(inp) - 1] and j not in [0, len(line) - 1]:
                
                #Checking left
                for x in line[:j][::-1]:
                    l += 1
                    if tree <= x:
                        break
                #Checking right
                for x in line[j+1:]:
                    r += 1
                    if tree <= x:
                        break
                #Checking up
                for x in sliced_arr[:i][::-1]:
                    u += 1
                    if tree <= x:
                        break
                #Checking down
                for x in sliced_arr[i+1:]:
                    d += 1
                    if tree <= x:
                        break
                
            tmp_score = l*r*u*d
            score = max(score, tmp_score)
            
    return score

#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")