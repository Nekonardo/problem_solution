# To avoid using too many stack,replace recursive calculation by a loop
def steps_to_reach_repeating_optimized(m):
    if m <= 0 or m % 1 != 0:
        print("Invalid input m, it must be a positive integer but it is: ", m)
    first_1_index = 0
    if m == 1:
        return 0
    old_value = m  # initial value
    while True:
        if old_value % 2 == 0:
            new_value = old_value / 2
        else:
            new_value = old_value * 3 + 1
        first_1_index += 1
        old_value = new_value
        if new_value == 1:
            return first_1_index


if __name__ == '__main__':
    for m in range(1, 10):
        print("m = ", m, " steps = ", steps_to_reach_repeating_optimized(m))
