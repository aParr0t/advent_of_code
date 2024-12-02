# ----------common for both parts
inp = [s.rstrip("\n") for s in open("input.txt")]
reports = [list(map(int, s.split(" "))) for s in inp]
# ----------common for both parts

# ----------part 1
total = 0
for r in reports:
    direction = r[1] - r[0]
    if direction < 0:
        span = [-3, -1]
    elif direction > 0:
        span = [1, 3]
    else:
        continue
    for i in range(len(r) - 1):
        step = r[i + 1] - r[i]
        if not span[0] <= step <= span[1]:
            break
    else:
        total += 1

print(f"Part 1 answer: {total}")
# ----------part 1


# ----------part 2
def is_report_safe(r: list, tolerance_count: int):
    if tolerance_count > 1:
        return False

    direction = r[1] - r[0]
    if direction < 0:
        span = [-3, -1]
    elif direction > 0:
        span = [1, 3]
    elif direction == 0:
        return is_report_safe(r[1:], tolerance_count + 1)

    for i in range(len(r) - 1):
        step = r[i + 1] - r[i]
        if not span[0] <= step <= span[1]:
            return is_report_safe(
                r[:i] + r[i + 1 :], tolerance_count + 1
            ) or is_report_safe(r[: i + 1] + r[i + 2 :], tolerance_count + 1)
    else:
        return True


total = 0
for r in reports:
    if len(r) <= 2:
        total += 1
        continue
    if is_report_safe(r, 0) or is_report_safe(r[1:], 1) or is_report_safe(r[:-1], 1):
        total += 1

print(f"Part 2 answer: {total}")
# ----------part 2
