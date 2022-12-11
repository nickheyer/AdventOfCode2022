import os
from collections import deque

#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):
    """Converting lines to usable input"""
    inp = list(map(lambda x: x.split(), txt.splitlines()))
    return [(line[0], int(line[1])) for line in inp]

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------

def part_one():
    inp = get_input("input.txt")

    max_y = max_x = min_y = min_x = 1

    for dir, distance in inp:
        if dir == "U":
            max_y += distance
        elif dir == "D":
            min_y += distance
        elif dir == "R":
            max_x += distance
        elif dir == "L":
            min_x += distance

    grid = [["."]*max(min_x, max_x) for _ in range(max(min_y, max_y))]
    grid[0][0] = "#"
    
    def print_grid():
        for k in grid[::-1]:
            print(f"{k}")
        print("-----------------\n")

    h = t = [0, 0] # X, Y (width, height)

    for dir, distance in inp:
        for i in range(distance):
            hx, hy = ox, oy = h
            
            # Moving Head
            if dir == "U":
                hy += 1
            elif dir == "D":
                hy -= 1
            elif dir == "R":
                hx += 1
            elif dir == "L":
                hx -= 1

            
            tx, ty = t
            # Calculating new location of tail
            
            # See if tail NEEDS to move
            if tx not in [hx-1,hx,hx+1] or ty not in [hy-1,hy,hy+1]:
                t = ox, oy
                grid[oy][ox] = "#"

            #print_grid()   
            h = hx, hy

    count = 0

    #Count grid
    for y in grid:
        count += y.count("#")

    return count



"""

For each segment of head->tail, if the tail is not touching the head and the tail is not in the
same row or column, move the tail diagonally. 

If the tail is not touching head but IS in the same row or column as the head, move it in the same direction as the head.

For the diagonal movement of the tail, in can be calculated as follows:

if tail-x is less than head-x and tail-y is less than head-y, increase tail-x and tail-y by one.
Else if tail-x greater than head-x and tail-y is less than head-y, decrement tail-x and increment tail-y.
Else if tail-x less than head-x and tail-y is greater than head-y, increment tail-x and decrement tail-y.
Else if tail-x greater than head-x and tail-y is greater than head-y, decrement tail-x and decrement tail-y.

"""


def part_two():
    inp = get_input("input.txt")

    y = x = 1

    max_width = min_width = max_height = min_height = 0

    for dir, distance in inp:
        if dir == "U":
            y += distance
            max_height = max(max_height, y)
        elif dir == "D":
            y -= distance
            min_height = min(min_height, y)
        elif dir == "R":
            x += distance
            max_width = max(max_width, x)
        elif dir == "L":
            x -= distance
            min_width = min(min_width, x)

    #Finding offset of grid/array and applying it to the origin, a hypothetical 0, 0
    origin = (abs(min_width) + 1, abs(min_height) + 1) # X, Y (Width, Height)
    ox, oy = origin

    grid = [["."]*(ox + max_width) for _ in range(oy + max_height)]
    grid[oy][ox] = "#"
    
    def print_grid():
        for k in grid[::-1]:
            print(f"{k}")
        print("-----------------\n")



    segments = [list(origin) for _ in range(10)] # Index 0 being the head, index 9 being the tail


    def move_head(head, dir):

        hx, hy = head

        # Moving Head
        if dir == "U":
            hy += 1
        elif dir == "D":
            hy -= 1
        elif dir == "R":
            hx += 1
        elif dir == "L":
            hx -= 1
        
        return hx, hy


    """
    If the tail is not touching head but IS in the same row or column as the head,
    move it in the same direction as the head.
    """
    def move_one(tail, head): # Tail X, Y and Head X, Y -> move tail one block towards Head.
        hx, hy = head
        tx, ty = tail

        if ty < hy:
            ty += 1
        elif ty > hy:
            ty -= 1
        elif tx < hx :
            tx += 1
        elif tx > hx:
            tx -= 1
        
        return tx, ty

    """
    For the diagonal movement of the tail, in can be calculated as follows:

    if tail-x is less than head-x and tail-y is less than head-y, increase tail-x and tail-y by one.
    Else if tail-x greater than head-x and tail-y is less than head-y, decrement tail-x and increment tail-y.
    Else if tail-x less than head-x and tail-y is greater than head-y, increment tail-x and decrement tail-y.
    Else if tail-x greater than head-x and tail-y is greater than head-y, decrement tail-x and decrement tail-y.
    """
    def move_diag(tail, head):
        hx, hy = head
        tx, ty = tail

        if tx < hx and ty < hy:
            tx += 1
            ty += 1
        elif tx > hx and ty < hy:
            tx -= 1
            ty += 1
        elif tx < hx and ty > hy:
            tx += 1
            ty -= 1
        elif tx > hx and ty > hy:
            tx -= 1
            ty -= 1
        
        return tx, ty



    """
    For each segment of head->tail, if the tail is not touching the head and the tail is not in the
    same row or column, move the tail diagonally. 

    If the tail is not touching head but IS in the same row or column as the head, 
    move it in the same direction as the head.
    """


    for dir, distance in inp:
        for i in range(distance): #Incrementing distance by one
            for seg in range(len(segments)):

                current = segments[seg]

                #Moving Head

                if seg == 0:
                    
                    segments[0] = move_head(current, dir)
                
                else:

                    head = segments[seg - 1]
                    tail = current

                    hx, hy = head
                    tx, ty = tail

                    #Find if tail and head are in same location, no movement
                    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
                        continue

                    #Find if tail is not touching head and in same row/col, move one
                    elif (abs(hx - tx) == 2 or abs(hy - ty) == 2) and (hx == tx or hy == ty):
                        segments[seg] = move_one(tail, head)
                    
                    #Head and tail arent touching and not in same row or col, move diagonally towards head
                    else:
                        segments[seg] = move_diag(tail, head)
                    
                    if seg == 9: #If the tail is the last segment, plot a # where it lands on the graph array
                        tx, ty = segments[9]

                        grid[ty][tx] = "#"

    count = 0

    #Count grid
    for y in grid:
        count += y.count("#")

    print_grid()

    return count


#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")