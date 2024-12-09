# ----------common for both parts
disk_map_inp = [s.strip("\n") for s in open("input.txt")][0]
# ----------common for both parts

# ----------part 1
checksum = 0
disk_map = disk_map_inp
l, r = 0, len(disk_map) - 1  # left and right pointer
li = 0  # precise index of left pointer
left_free_left = None  # how much free space is left in left pointer
right_file_left = None  # how much file is left in right pointer
while l < r:
    l_is_file = l % 2 == 0
    r_is_file = r % 2 == 0
    l_id = l // 2
    r_id = r // 2
    lw = int(disk_map[l])
    if l_is_file:
        # since left pointer is file, add it to the checksum and move on
        check = 0
        for h in range(li, li + lw):
            check = h * l_id
            checksum += check
        l += 1
        li += lw
        left_free_left = None
    else:
        # left pointer is empty space, so move blocks from right pointer here
        if left_free_left is None:
            left_free_left = lw

        if r_is_file:
            # right pointer is a file, so move it to the left pointer
            if right_file_left is None:
                right_file_left = int(disk_map[r])

            # the amount of blocks to move will be the
            # minimum of free space available in left pointer and
            # the number of blocks to move from right pointer
            w = min(left_free_left, right_file_left)

            # add to checksum
            for h in range(li, li + w):
                check = h * r_id
                checksum += check
            # update left pointer free space and right pointer blocks left
            li += w
            left_free_left -= w
            right_file_left -= w

            if right_file_left == 0:
                # if all of the right file has been moved, decrement
                r -= 1
                right_file_left = None
            if left_free_left == 0:
                # if all space is used in left pointer, increment
                l += 1
                left_free_left = None
        else:
            # right pointer is free space, so don't move anything
            r -= 1
            right_file_left = None

# it may happen that not all of the right file got
# moved to free space on the left, so add it to the checksum
if right_file_left and right_file_left != 0:
    for h in range(li, li + right_file_left):
        check = h * r_id
        checksum += check

print(f"Part 1 answer: {checksum}")
# ----------part 1

# ----------part 2
checksum = 0
l = 0
li = 0
left_free_left = None
disk_map = [int(x) for x in disk_map_inp]
while l < len(disk_map):
    l_is_file = (l % 2 == 0) and disk_map[l] != "#"
    l_id = l // 2
    if disk_map[l] != "#":
        lw = disk_map[l]
    if l_is_file:
        # since left pointer is file, add it to the checksum and move on
        check = 0
        for h in range(li, li + lw):
            check = h * l_id
            checksum += check
        l += 1
        li += lw
        left_free_left = None
    else:
        # Left pointer is free space. Go from right to left
        # and find the first file that fits into this free space.
        # If such a file is found, then move it to this free space and
        # add it to the checksum. Otherwise increment left pointer
        if left_free_left is None:
            left_free_left = lw
        for r in range(len(disk_map), l, -1):
            r_is_file = (r % 2 == 0) and disk_map[r] != "#"
            if not r_is_file:
                continue
            r_id = r // 2
            w = disk_map[r]
            if w <= left_free_left:
                for h in range(li, li + w):
                    check = h * r_id
                    checksum += check
                li += w
                left_free_left -= w
                # mark this file as moved so it doesn't get moved again
                disk_map[r] = "#"
                if left_free_left == 0:
                    l += 1
                    left_free_left = None
                break
        else:
            # if no file was found that fits in the free space
            # then increment the left pointer
            l += 1
            li += left_free_left
            left_free_left = None

print(f"Part 2 answer: {checksum}")
# ----------part 2
