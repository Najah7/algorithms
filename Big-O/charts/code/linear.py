"""Generate a linear chart."""

import numpy as np
from utils import generate_chart

OUTPUT = "linear.png"

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
label = "Linear"
big_o = n

generate_chart(n, big_o, label, OUTPUT)
