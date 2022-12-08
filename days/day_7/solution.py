import os


#------------- ~ INPUT HANDLING ~ --------------

def parse_input(txt):

    """Converting lines to usable input"""
    
    log = list()

    for line in txt.splitlines():
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                log.append(line[1:])
        else:
            log.append(line)
    
    return log

def get_input(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as fp:
        return parse_input(fp.read())

#-------------- ~ SOLUTIONS ~ -------------------
class File:

    def __init__(self, file_name, size, dir) -> None:
        self.file_name = file_name
        self.prev = dir
        self.size = size

    def __repr__(self) -> str:
        return self.file_name

class Filesystem:

    def __init__(self, dir_name, root=False, prev=None) -> None:
        self.dir_name = dir_name
        self.children = list()
        self.current_dir = self
        self.total_size = 0
        if root:
            self.root_dir = self
            self.prev = self
        else:
            self.root_dir = prev.root_dir
            self.prev = prev

    def __repr__(self) -> str:
        return self.dir_name

    @staticmethod
    def rec_tree(node, nesting_level = 0, verbose = False):
        if type(node) == File:
            s = f" (File) | Size: {node.size}" if verbose else ""
            return f"{'  '*nesting_level}- {node.file_name}{s}\n "
        else:
            s = f" (Dir) | Size: {node.total_size}" if verbose else ""
            path = f"{'  '*nesting_level}- {node.dir_name}{s}\n "
            for n in node.children:
                if n != None:
                    path += Filesystem.rec_tree(n, nesting_level+1, verbose)
            return path
        
    @staticmethod
    def sum_dir_size(node, max_size):
        if type(node) == File:
            return 0
        else:
            size = 0
            if node.total_size <= max_size:
                size += node.total_size
            for n in node.children:
                if type(n) == Filesystem:
                    size += Filesystem.sum_dir_size(n, max_size)
            return size


    def add_dir(self, name):
        node = self.current_dir
        new_node = Filesystem(name, prev=node)
        node.children.append(new_node)
        return new_node

    def change_dir(self, name):
        if name == "..":
            self.current_dir = self.current_dir.prev
        elif name == "/":
            self.current_dir = self.root_dir
        else:
            try:
                self.current_dir = list(filter(lambda d: str(d) == name and type(d) == Filesystem
                , self.current_dir.children))[0]
            except Exception as e:
                print(f"Name: {name}, Current_Dir: {self.current_dir}")
                print("No directory exists ", e)

    def add_file(self, name, size):
        t_node = node = self.current_dir
        node.total_size += size
        while (t_node != self.root_dir):
            t_node.prev.total_size += size
            t_node = t_node.prev

        new_node = File(name, size, node)
        node.children.append(new_node)
        return new_node

    @staticmethod
    def find_deletion_options(node, size_needed, closest):
        if type(node) == File:
            return 0
        else:
            if node.total_size >= size_needed and closest > node.total_size:
                closest = node.total_size
            for n in node.children:
                if type(n) == Filesystem:
                    tmp = Filesystem.find_deletion_options(n, size_needed, closest)
                    if tmp >= size_needed and closest > tmp:
                        closest = tmp
            return closest

def load_fs():
    inp = get_input("input.txt")
        
    filesystem = Filesystem("/", root=True)

    for log in inp:
        if log[0] == "cd":
            filesystem.change_dir(log[1])
        elif log[0] == "dir":
            filesystem.add_dir(log[1])
        else:
            filesystem.add_file(log[1], int(log[0]))

    print(Filesystem.rec_tree(filesystem, verbose=True))
    return filesystem
                

def part_one():
    fs = load_fs()
    return Filesystem.sum_dir_size(fs, 100_000)


def part_two():
    fs = load_fs()
    current_size = fs.total_size
    return Filesystem.find_deletion_options(fs, current_size - 40_000_000, current_size)

#-------------- ~ RESULTS ~ -------------------

print(f"Part One: {part_one()}\nPart Two: {part_two()}")