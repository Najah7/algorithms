"""Generate an exponential chart."""

import numpy as np
from utils import generate_chart

OUTPUT = "exponential.png"

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
label = "Exponential"
big_o = 2**n

generate_chart(n, big_o, label, OUTPUT)
