"""Generate a chart of the factorial function."""

import numpy as np
from utils import generate_chart

OUTPUT = "fatorial.png"

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
label = "Fatorial"
big_o = n

generate_chart(n, big_o, label, OUTPUT)
