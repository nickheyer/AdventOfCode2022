import os
import math

#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):
    """Converting lines to usable input"""
    inp = [list(map(lambda x: ord(x)-97 if x not in ["S", "E"] else x, j)) for j in txt.splitlines()]
    origin, dest = None, None

    for y, j in enumerate(inp):
        for x, k in enumerate(j):
            
            if k == "S":
                origin = [x, y]
                inp[y][x] = 0
            elif k == "E":
                dest = [x, y]
                inp[y][x] = 25

    return inp, origin, dest
    
        


def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------


def part_one():
    inp, origin, dest = get_input("input.txt")

    unvisited = set()

    distance = dict()

    dest_str = f"{dest[0]},{dest[1]}"

    for y, j in enumerate(inp):
        for x, k in enumerate(j):

            node = f"{x},{y}"

            unvisited.add(node)

            if [x,y] == origin:
                distance[node] = 0
            else:
                distance[node] = math.inf


    while len(unvisited) != 0:

        #Find node with smallest distance

        smallest_distance_node = None
        for n in unvisited:
            if smallest_distance_node == None or distance[n] < distance[smallest_distance_node]:
                smallest_distance_node = n
        
        unvisited.remove(smallest_distance_node)

        #Get neighbors of smallest node, if the neighbor is with +/- 0 steps

        neighbors = list()

        for n in unvisited:
            nx,ny = list(map(lambda j: int(j), n.split(",")))
            ux, uy = list(map(lambda j: int(j), smallest_distance_node.split(",")))


            
            if [ux, uy] in [[nx-1, ny], [nx+1, ny], [nx, ny-1], [nx, ny+1]]:
                neighbors.append(f"{nx},{ny}")

        #For each neighbor of smallest distance node, set its distance from origin to be distance of smallest node + 1, IF its distance is currently GREATER than smallest node distance + 1

        for v in neighbors:
            nx,ny = list(map(lambda j: int(j), v.split(",")))
            ux, uy = list(map(lambda j: int(j), smallest_distance_node.split(",")))
            n_node = inp[ny][nx]
            o_node = inp[uy][ux]
            
            if n_node <= o_node + 1:
                alt = distance[smallest_distance_node] + 1
                if alt < distance[v]:
                    distance[v] = alt

    return distance[dest_str]

def part_two():
    inp, origin, dest = get_input("input.txt")

    unvisited = set()

    distance = dict()

    for y, j in enumerate(inp):
        for x, k in enumerate(j):

            node = f"{x},{y}"

            unvisited.add(node)

            if [x,y] == dest:
                distance[node] = 0
            else:
                distance[node] = math.inf


    while len(unvisited) != 0:

        #Find node with smallest distance

        smallest_distance_node = None
        for n in unvisited:
            if smallest_distance_node == None or distance[n] < distance[smallest_distance_node]:
                smallest_distance_node = n
        
        unvisited.remove(smallest_distance_node)

        #Get neighbors of smallest node, if the neighbor is with +/- 0 steps

        neighbors = list()

        for n in unvisited:
            nx,ny = list(map(lambda j: int(j), n.split(",")))
            ux, uy = list(map(lambda j: int(j), smallest_distance_node.split(",")))


            
            if [ux, uy] in [[nx-1, ny], [nx+1, ny], [nx, ny-1], [nx, ny+1]]:
                neighbors.append(f"{nx},{ny}")

        #For each neighbor of smallest distance node, set its distance from origin to be distance of smallest node + 1, IF its distance is currently GREATER than smallest node distance + 1

        for v in neighbors:
            nx,ny = list(map(lambda j: int(j), v.split(",")))
            ux, uy = list(map(lambda j: int(j), smallest_distance_node.split(",")))
            n_node = inp[ny][nx]
            o_node = inp[uy][ux]
            
            if n_node >= o_node - 1:
                alt = distance[smallest_distance_node] + 1
                if alt < distance[v]:
                    distance[v] = alt


    #Get list of all nodes at elevation 0
    smallest_a = math.inf

    for y, j in enumerate(inp):
        for x, k in enumerate(j):
            dest_str = f"{x},{y}"
            if inp[y][x] == 0: # is a
                smallest_a = min(smallest_a, distance[dest_str])

    return smallest_a

#-------------- ~ RESULTS ~ -------------------

print(f"\nPart One: {part_one()}\n\nPart Two: {part_two()}")