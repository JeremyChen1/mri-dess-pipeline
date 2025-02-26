from math import exp
import numpy as np
import matplotlib.pyplot as plt

def DESS_Meniscus(TR_DESS, TE_DESS, FA_DESS, T1_Meniscus, T2_Meniscus, PD):
    """Simulate DESS MRI signal."""
    E1_Meniscus = np.exp(-TR / T1_Meniscus)
    E2_Meniscus = np.exp(-TE / T2_Meniscus)
    r_meniscus = sqrt((1 - E2_meniscus^2) / ((1 - E1_meniscus * cos(FA_DESS))^2 - E2_meniscus^2 * (E1_meniscus - cos(FA_DESS))^2));
    S2_S1_Ratio = exp(-2*(TR_DESS - TE_DESS)/T2_Meniscus)
    S_plus = PD * (1 - E1_Meniscus) * np.sin(FA_DESS) / (1 - E1_Meniscus * np.cos(FA_DESS))
    S_minus = S_plus * E2_Meniscus
    return S_plus, S_minus

# Example parameters
TR_DESS = 15e-3  # Repetition Time (s)
TE_DESS = 5e-3   # Echo Time (s)
FA_DESS = np.deg2rad(30)  # Flip Angle (rad)
T1_Cartilage = 900 # ms
T1_Meniscus = 960 # ms
T2_Cartilage = 39 # ms  
T2_Meniscus = 26.7 # ms
PD = 1.0      # Proton Density

S_plus, S_minus = DESS_Meniscus(TR, TE, FA, T1, T2, PD)

# Plot results
plt.figure()
plt.bar(["S_plus", "S_minus"], [S_plus, S_minus])
plt.title("DESS Signal Simulation")
plt.ylabel("Signal Intensity")
plt.show()

