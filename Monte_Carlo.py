import numpy as np
import matplotlib.pyplot as plt
from dess_simulation import dess_signal  # Import from our previous script

def monte_carlo_simulation(n_samples=1000):
    """Perform Monte Carlo simulation for DESS signal variations."""
    TR = 15e-3  # Repetition Time (s)
    TE = 5e-3   # Echo Time (s)
    FA = np.deg2rad(30)  # Flip Angle (rad)
    PD = 1.0  # Proton Density

    # Generate random T1 and T2 values
    T1_values = np.random.normal(1000e-3, 50e-3, n_samples)  # Mean 1000ms, std 50ms
    T2_values = np.random.normal(80e-3, 5e-3, n_samples)  # Mean 80ms, std 5ms

    S_plus_samples = []
    S_minus_samples = []

    for T1, T2 in zip(T1_values, T2_values):
        S_plus, S_minus = dess_signal(TR, TE, FA, T1, T2, PD)
        S_plus_samples.append(S_plus)
        S_minus_samples.append(S_minus)

    # Plot histogram of results
    plt.hist(S_plus_samples, bins=50, alpha=0.7, label="S_plus")
    plt.hist(S_minus_samples, bins=50, alpha=0.7, label="S_minus")
    plt.legend()
    plt.title("Monte Carlo Simulation of DESS")
    plt.xlabel("Signal Intensity")
    plt.ylabel("Frequency")
    plt.show()

# Run Monte Carlo simulation
monte_carlo_simulation()

