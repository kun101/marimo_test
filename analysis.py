# analysis.py
# Author: blakpot32@gmail.com
# A simple Marimo notebook demonstrating interactivity and dependencies

import marimo as mo

# Cell 1: Define interactive widget (input)
slider = mo.ui.slider(1, 100, value=10, label="Select number of points")

# Cell 2: Create dependent variable (data generation)
# This depends on slider.value
import numpy as np
x = np.linspace(0, 10, slider.value)
y = np.sin(x)

# Cell 3: Dynamic markdown output based on widget state
# This depends on both the slider and data
mo.md(f"""
### Interactive Sine Wave Demo

- Number of points: **{slider.value}**
- Data shape: **{x.shape}**
- Visual indicator: {"🟢" * (slider.value // 5)}

""")

# Cell 4: Plot data (depends on x, y)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")
ax.legend()
mo.output(fig)
