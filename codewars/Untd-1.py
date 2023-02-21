def part_checker(part):
    for x in range(1, 10):
        if x not in part:
            return False
    return True