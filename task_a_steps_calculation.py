# Definition by the task description, by induction

def value_at_n(n, m):
    if n == 0:  # recursion initial condition
        return m
    c_m_n = value_at_n(n - 1, m)
    if c_m_n % 2 == 0:
        return int(c_m_n / 2)
    else:
        return int((c_m_n * 3) + 1)


# It can be notice that once reach number 1 for the first time
# the next element must be 2 and start iteration. Thus returning
# the index is sufficient.
def steps_to_reach_repeating(m):
    if m <= 0 or m % 1 != 0:
        print("Invalid input m, it must be a positive integer but it is: ", m)

    first_1_index = 0
    while True:
        if value_at_n(first_1_index, m) != 1:
            first_1_index += 1
        else:
            return first_1_index


if __name__ == '__main__':
    for m in range(1, 10):
        print("m = ", m, " steps = ", steps_to_reach_repeating(m))

