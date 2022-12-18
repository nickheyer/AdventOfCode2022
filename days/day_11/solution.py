import os
import math

#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):
    """Converting lines to usable input"""
    inp = txt.splitlines()
    monkeys = dict()

    for x, i in enumerate(range(0, len(inp), 7)):
        m = inp[i:i+7]
        monkeys[x] = dict()
        monkeys[x]["items"] = [int(x.strip()) for x in m[1].split(":")[1].split(",")]

        op = m[2].split("=")[1][5:].split()
        monkeys[x]["operator"] = op[0]
        monkeys[x]["op_int"] = op[1].strip()
        monkeys[x]["test"] = int(m[3].split("by")[1].strip())
        monkeys[x]["test_true"] = int(m[4].split("monkey")[1].strip())
        monkeys[x]["test_false"] = int(m[5].split("monkey")[1].strip())

    return monkeys
        


def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------



class Monkey:

    monkey_list = list()
    s_divisor = set()

    def __init__(self, num, items, op, op_i, test_d, test_true, test_false, worry_reduction = True) -> None:
        self.number = num
        self.items = items
        self.op = op
        self.op_i = op_i if op_i == "old" else int(op_i)
        self.test_d = test_d
        Monkey.s_divisor.add(test_d)
        self.test_true = test_true
        self.test_false = test_false
        self.activity = 0
        self.worry_reduction = worry_reduction
        Monkey.monkey_list.append(self)

    def __mul__(self, other):
        return self.activity * other.activity

    def __repr__(self) -> str:
        return f"monkey {self.number}"

    def inspect(self, item, verbose):

        old = item
        self.activity += 1

        if self.op == "*":
            old = old * self.op_i if self.op_i != "old" else old ** 2
        elif self.op == "+":
            old = old + self.op_i if self.op_i != "old" else old + old


        debug = f"Monkey {self.number} inspects item with worry level of {item}"
        if verbose and self.worry_reduction: 
            print(debug + f", increases to {old}, worry level reduced to {old // 3}")
        elif verbose:
            print(debug)

        return old // 3 if self.worry_reduction else old % math.prod(Monkey.s_divisor) # <- The trick to part 2...

    def test(self, item, verbose):

        item = self.inspect(item, verbose)

        if item % self.test_d == 0:
            if verbose: print(f"Worry level {item} is divisible by {self.test_d}, thrown to monkey {self.test_true}")
            Monkey.monkey_list[self.test_true].items.append(item)

        else:
            if verbose: print(f"Worry level {item} is NOT divisible by {self.test_d}, thrown to monkey {self.test_false}")
            Monkey.monkey_list[self.test_false].items.append(item)


    def inspect_items(self, verbose = False):
        for i, item in enumerate(self.items):
            self.test(item, verbose)
        
        self.items = list()

    @staticmethod
    def active_monkeys():
        return "\n" + "\n".join([f"Monkey {x.number} inspected items {x.activity} times | {x.items}" 
        for x in sorted(Monkey.monkey_list, key=lambda k: k.activity, reverse = True)]) + "\n"

    @staticmethod
    def two_most_active():
        m1, m2 = sorted(Monkey.monkey_list, key=lambda k: k.activity, reverse = True)[:2]
        return f"\nThe current level of monkey business is: {m1 * m2}\nTop contributors were: {m1} ({m1.activity}) and {m2} ({m2.activity})"


def load_monkeys(file_name, wr=True):
    inp = get_input(file_name)  
    if Monkey.monkey_list:
        Monkey.monkey_list = list()
    for i, m in inp.items():
        Monkey(i, m["items"], m["operator"], m["op_int"], m["test"], m["test_true"], m["test_false"], worry_reduction=wr) 

def part_one():
    load_monkeys("input.txt")

    rounds = 20

    for _round in range(rounds):
        
        for monkey in Monkey.monkey_list:
            monkey.inspect_items(verbose = False)

    return Monkey.two_most_active()

def part_two():
    load_monkeys("input.txt", wr=False)

    rounds = 10000

    for _round in range(rounds):
        
        for monkey in Monkey.monkey_list:
            monkey.inspect_items(verbose = False)

    return Monkey.two_most_active()


#-------------- ~ RESULTS ~ -------------------

print(f"\nPart One: {part_one()}\n\nPart Two: {part_two()}")