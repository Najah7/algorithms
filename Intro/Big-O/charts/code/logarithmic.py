"""Generate logarithmic charts."""

import numpy as np
from utils import generate_chart

OUTPUT = "logarithmic.png"

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
label = "Logarithmic"
big_o = np.log(n)

generate_chart(n, big_o, label, OUTPUT)
