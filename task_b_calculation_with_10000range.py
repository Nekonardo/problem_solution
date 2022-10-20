import time
from task_a_steps_calculation import steps_to_reach_repeating
from task_c_steps_calculation_optimized import steps_to_reach_repeating_optimized

N = 10000


def original_method(n):
    for x in range(1, n):
        steps_to_reach_repeating(x)


def optimized_method(n):
    for x in range(1, n):
        steps_to_reach_repeating_optimized(x)


if __name__ == '__main__':
    # approximately 20secs in total, for reference
    print("Process starts")
    starting_time = time.time()
    original_method(N)
    print("Original method took: ", time.time() - starting_time)

    starting_time = time.time()
    optimized_method(N)
    print("Optimized method took: ", time.time() - starting_time)
    print("Process ends")
