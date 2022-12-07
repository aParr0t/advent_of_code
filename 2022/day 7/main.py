# read input
console_log = [s.rstrip("\n") for s in open("input.txt")]

# ----------both parts


class Directory:
    def __init__(self, name: str, parent) -> None:
        self.parent = parent
        self.name = name
        self.children = {}
        self.size = 0


class File:
    def __init__(self, name: str, size: int, parent: Directory) -> None:
        self.name = name
        self.parent = parent
        self.size = size


filesystem = Directory(name="/", parent=None)
current_dir = filesystem
for line in console_log:
    tokens = line.split(" ")
    # print(f"line: {line}")
    if line.startswith("$ ls"):
        continue
    elif line.startswith("$ cd"):
        path = tokens[-1]
        if path == "/":
            current_dir = filesystem
        elif path == "..":
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.children[path]
    elif tokens[0] == "dir":
        dir_name = tokens[1]
        current_dir.children[dir_name] = Directory(
            name=dir_name, parent=current_dir
        )
    elif tokens[0].isnumeric():
        file_size = int(tokens[0])
        file_name = tokens[1]
        current_dir.children[file_name] = File(
            name=file_name, size=file_size, parent=current_dir
        )


# ----------both parts

# ----------part 1
size_sum = 0
small_size_limit = 100000


def calculate_size(directory: Directory):
    global size_sum
    total_size = 0
    for child in directory.children.values():
        if isinstance(child, Directory):
            total_size += calculate_size(child)
        elif isinstance(child, File):
            total_size += child.size
    directory.size = total_size
    if total_size <= small_size_limit:
        size_sum += total_size
    return total_size


calculate_size(filesystem)
print(f"Part 1 answer: {size_sum}")
# ----------part 1

# ----------part 2
sizes = []


def calculate_size(directory: Directory):
    global size_sum
    total_size = 0
    for child in directory.children.values():
        if isinstance(child, Directory):
            total_size += calculate_size(child)
        elif isinstance(child, File):
            total_size += child.size
    directory.size = total_size
    sizes.append(total_size)
    return total_size


total_disk_space = 70_000_000
req_space = 30_000_000
calculate_size(filesystem)
free_space = total_disk_space - filesystem.size
alloc_space = req_space - free_space
sizes = [x for x in sorted(sizes) if x >= alloc_space]
smallest_delete_size = sizes[0]

print(f"Part 2 answer: {smallest_delete_size}")
# ----------part 2
