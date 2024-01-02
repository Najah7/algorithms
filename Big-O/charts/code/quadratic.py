"""Generate a quadratic chart."""

import numpy as np
from utils import generate_chart

OUTPUT = "quadratic.png"

n = np.linspace(1, 10, 1000)
label = "Quadratic"
big_o = n**2

generate_chart(n, big_o, label, OUTPUT)
