# Definition by the task description, by recursion

def value_at_n(n, m):
    if m <= 0 or m % 1 != 0:
        raise Exception("Invalid input m, it must be a positive integer but it is: ", m)

    if n == 0:  # recursion terminating condition
        return m

    last_element_in_sequence = value_at_n(n - 1, m)
    if last_element_in_sequence % 2 == 0:
        return int(last_element_in_sequence / 2)
    else:
        return int((last_element_in_sequence * 3) + 1)


# It can be noticed that once reach number 1 for the first time
# the next element must be 2 and start '1,2,4,1,2...' iteration
# Thus returning the index of first 1 is sufficient

# Steps calculated here referred to steps from n = 1 to first
# required element
def steps_to_reach_repeating(m):
    if m <= 0 or m % 1 != 0:
        raise Exception("Invalid input m, it must be a positive integer but it is: ", m)

    first_1_index = 0
    while True:
        if value_at_n(first_1_index, m) != 1:
            first_1_index += 1
        else:
            return first_1_index


if __name__ == '__main__':
    for m in range(0, 10):
        print("m = ", m, " steps = ", steps_to_reach_repeating(m))

