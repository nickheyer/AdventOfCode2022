import sys
import os

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return fp.read()

def part_one():
    inp = get_input("input.txt").splitlines()
    sample = """A Y
B X
C Z""".splitlines()

    score = 0
    # Rock, Paper, Scissors, Rock, Paper, Scissors
    choices = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
    
    for round in inp:

        opp, _, player = round

        if choices[opp] == choices[player]:
            score += 3 
        elif opp == "A": #Opp chose rock     
            if player == "Y": #Player chose paper
                score += 6
        elif opp == "B":   
            if player == "Z":
                score += 6
        elif player == "X":
            score += 6
        
        score += choices[player]

        #print(round)


    return score



def part_two():
    inp = get_input("input.txt").splitlines()
    sample = """A Y
B X
C Z""".splitlines()

    score = 0
    # Rock, Paper, Scissors
    choices = {"A": 1, "B": 2, "C": 3}
    
    for round in inp:

        opp, _, decider = round

        if decider == "Y":
            score += 3 + choices[opp]
        elif decider == "X":   
            if opp == "A":
                score += 3
            elif opp == "B":   
                score += 1
            else:
                score += 2
        else:
            score += 6
            if opp == "A":
                score += 2
            elif opp == "B":   
                score += 3
            else:
                score += 1


        #print(round)


    return score





print(part_two())