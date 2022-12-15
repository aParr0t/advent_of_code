# read input
inp = [s.rstrip("\n") for s in open("input.txt")]


# ----------both parts
# init sensors
sensor_data = []
for s in inp:
    tokens = s.split(" ")
    sensor_x = int(tokens[2][2:-1])
    sensor_y = int(tokens[3][2:-1])
    beacon_x = int(tokens[8][2:-1])
    beacon_y = int(tokens[9][2:])
    sensor_data.append(
        {
            "pos": (sensor_x, sensor_y),
            "nearest_beacon": (beacon_x, beacon_y),
        }
    )

# init distances
sensor_distance_data = []
for data in sensor_data:
    sx, sy = data["pos"]
    bx, by = data["nearest_beacon"]
    x_dist, y_dist = abs(bx - sx), abs(by - sy)
    sensor_distance_data.append({"pos": (sx, sy), "distance": x_dist + y_dist})


def range_union(a, b):
    x1, x2 = a
    x3, x4 = b
    if x1 > x4 or x2 < x3:
        return -1
    return [min(x1, x3), max(x2, x4)]


def sensor_overlaps_y(y):
    overlap_ranges = []
    for data in sensor_distance_data:
        sx, sy = data["pos"]
        max_dist = data["distance"]

        dist_from_y = abs(y - sy)
        if dist_from_y > max_dist:
            continue

        max_x_offset = max_dist - dist_from_y
        overlap_range = (sx - max_x_offset, sx + max_x_offset)
        overlap_ranges.append(overlap_range)
    return overlap_ranges


def merge_overlaps(overlaps):
    for i in range(len(overlaps) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            union = range_union(overlaps[i], overlaps[j])
            if union == -1:
                continue

            overlaps[i] = union
            del overlaps[j]
            break
    return overlaps


# ----------both parts

# ----------part 1
check_y = 2000000
overlap_ranges = sensor_overlaps_y(check_y)
overlap_ranges = merge_overlaps(overlap_ranges)

# count number of positions that can't contain a beacon
filled_range_sum = 0
for filled_range in overlap_ranges:
    filled_range_sum += filled_range[1] - filled_range[0] + 1

unique_beacons = set()
for data in sensor_data:
    unique_beacons.add(data["nearest_beacon"])
filled_range_sum -= [beacon[1] for beacon in unique_beacons].count(check_y)

print(f"Part 1 answer: {filled_range_sum}")
# ----------part 1

# ----------part 2
boundary = 4000000
for check_y in range(0, boundary + 1):
    overlap_ranges = sensor_overlaps_y(check_y)
    overlap_ranges = merge_overlaps(overlap_ranges)

    # count number of positions that can't contain a beacon
    filled_range_sum = 0
    for x1, x2 in overlap_ranges:
        if x2 < 0 or x1 > boundary:
            continue
        filled_range_sum += min(boundary, x2) - max(0, x1) + 1

    if filled_range_sum == boundary + 1:
        continue

    # found the row that contains the stress beacon
    # find the x-coordinate of the beacon
    possible_x_values = set(range(0, boundary + 1))
    for x1, x2 in overlap_ranges:
        filled_set = set(range(max(0, x1), min(boundary, x2) + 1))
        possible_x_values.difference_update(filled_set)

    beacon_x, beacon_y = list(possible_x_values)[0], check_y
    break

tuning_frequency = beacon_x * 4000000 + beacon_y

print(f"Part 2 answer: {tuning_frequency}")
# ----------part 2
