import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from task_a_steps_calculation import steps_to_reach_repeating
from task_c_steps_calculation_optimized import steps_to_reach_repeating_optimized

# N is the maximum range of parameter m
N = 10000

# Plot the diagram interactively
if __name__ == '__main__':
    print("Process starts")
    starting_time = time.time()
    # original_method(n)
    x_data = np.linspace(1, N, N, dtype=int)
    y_data = np.asarray([steps_to_reach_repeating_optimized(i) for i in x_data])
    df = pd.DataFrame({'Value of m': x_data, 'Steps to reach repetition': y_data})

    fig = px.scatter(df, x='Value of m', y='Steps to reach repetition',
                     title="Steps to reach 1 the first time in repetition")
    fig.show()
    print("Plotting took: ", time.time() - starting_time)
    print("Process ends")
