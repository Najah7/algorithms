"""Generate a constant chart."""

import numpy as np
from utils import generate_chart

OUTPUT = "constant.png"

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
label = "Constant"
big_o = np.ones(n.shape)

generate_chart(n, big_o, label, OUTPUT)
