import matplotlib.pyplot as plt
import numpy as np


def plot_data(x, y, title="Data Plot", xlabel="X-axis", ylabel="Y-axis"):
    """Plot the given x and y data."""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the example data
    plot_data(x, y, title="Sine Wave", xlabel="Time", ylabel="Amplitude")