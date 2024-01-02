"""Gnerate a log-linear chart."""

import numpy as np
from utils import generate_chart

OUTPUT = "log_linear.png"

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
label = "Log Linear"
big_o = n * np.log(n)

generate_chart(n, big_o, label, OUTPUT)
