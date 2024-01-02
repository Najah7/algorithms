"""Utility functions for generating charts."""

import pathlib

import matplotlib.pyplot as plt
import numpy as np

image_dir = pathlib.Path(__file__).parent.parent / "image"


def generate_chart(n: np.ndarray, big_o: np.ndarray, label: str, output: str) -> None:
    """Generate a chart comparing the runtimes of different functions."""
    # Plot setup
    plt.figure(figsize=(12, 10))
    plt.ylim(0, 20)

    # Plot each function
    plt.plot(n, big_o, label=label)

    # Plot labels
    plt.legend(loc=0)
    plt.ylabel("Relative Runtime")

    # Save image
    plt.savefig(f"{image_dir}/{output}")
