import numpy as np
import matplotlib.pyplot as plt

def dess_signal(TR, TE, FA, T1, T2, PD):
    """Simulate DESS MRI signal."""
    E1 = np.exp(-TR / T1)
    E2 = np.exp(-TE / T2)
    S_plus = PD * (1 - E1) * np.sin(FA) / (1 - E1 * np.cos(FA))
    S_minus = S_plus * E2
    return S_plus, S_minus

# Example parameters
TR = 15e-3  # Repetition Time (s)
TE = 5e-3   # Echo Time (s)
FA = np.deg2rad(30)  # Flip Angle (rad)
T1 = 1000e-3  # T1 relaxation time (s)
T2 = 80e-3    # T2 relaxation time (s)
PD = 1.0      # Proton Density

S_plus, S_minus = dess_signal(TR, TE, FA, T1, T2, PD)

# Plot results
plt.figure()
plt.bar(["S_plus", "S_minus"], [S_plus, S_minus])
plt.title("DESS Signal Simulation")
plt.ylabel("Signal Intensity")
plt.show()

