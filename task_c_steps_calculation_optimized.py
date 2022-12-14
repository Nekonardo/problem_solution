# To avoid using too many stacks,I replaced recursive calculation by using a loop
def steps_to_reach_repeating_optimized(m):
    if m <= 0 or m % 1 != 0:
        print("Invalid input m, it must be a positive integer but it is: ", m)

    first_1_index = 1
    if m == 1:
        return first_1_index
    old_value = m  # initial last_element_value is set to m
    while True:
        if old_value % 2 == 0: # if last_element_value is even
            new_value = old_value / 2
        else:
            new_value = old_value * 3 + 1
        first_1_index += 1
        old_value = new_value
        if new_value == 1:
            return first_1_index


if __name__ == '__main__':
    # example of usage from m = 1 to m = 10
    for m in range(1, 10):
        print("m = ", m, " steps = ", steps_to_reach_repeating_optimized(m))
