# Problem solution

This repsitory is a solution for the sample coding task and following presentation.

## Installation

Use [git clone](https://github.com/git-guides/git-clone) under the desired path get the repository and run under your
Python(3.8 or above) environment.

```bash
git clone https://github.com/Nekonardo/problem_solution.git
```

Note packages in requirement.txt are needed before execution. For example, plotly.py may be installed using pip.

```bash
pip install plotly==5.9.0
```

## Usage

### Task (a)

To get $C_m(n)$ value with given n and m.

```python
    value = value_at_n(n, m)
```

Calculate minimum steps needed for different m value, from m = 1 to m = 10.

```python

for m in range(1, 10):
    print("m = ", m, " steps = ", steps_to_reach_repeating(m))
```

### Task (b)

Calculate minimum steps to reach repetition via original method from m = 1 to m = N, where N = 10000.

```python

N = 10000
original_method(N)
```

### Task (c)

Similar to function in task (a), function steps_to_reach_repeating_optimized(m) is used to calculate minimum steps to
 repetition, in a optimized way.


```python
    for m in range(1, 10):
    print("m = ", m, " steps = ", steps_to_reach_repeating_optimized(m))
```

### Task (d)

Mapping m to x-axis with range of [1,10000]  and coresponding minimum steps $n_{min} s.t C_m(n) =1$ to y-axis, the
scatter diagram can be plotted in the following way.

```python 
    x_data = np.linspace(1, N, N, dtype=int)
    y_data = np.asarray([steps_to_reach_repeating_optimized(i) for i in x_data])
    df = pd.DataFrame({'Value of m': x_data, 'Steps to reach repetition': y_data})

    fig = px.scatter(df, x='Value of m', y='Steps to reach repetition',
                     title="Steps to reach 1 the first time in repetition")
    fig.show()
```

## Contributing

Pull requests are welcome. For bug fix, please open an issue first to discuss what you would like to change.

## License

No license is declared explicitly, here I use [MIT](https://choosealicense.com/licenses/mit/) as an example license.

The repository is for temporary use only and will be deleted soon.
