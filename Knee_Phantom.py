import numpy as np
import matplotlib.pyplot as plt

def generate_knee_phantom(size=128):
    """Create a synthetic knee MRI phantom."""
    phantom = np.zeros((size, size))

    # Simulate cartilage (bright region)
    cartilage_x, cartilage_y = np.meshgrid(np.linspace(-1, 1, size), np.linspace(-1, 1, size))
    cartilage_mask = (cartilage_x**2 + cartilage_y**2) < 0.6
    phantom[cartilage_mask] = 0.8  # Higher intensity for cartilage

    # Simulate meniscus (dark region)
    meniscus_mask = (cartilage_x**2 + cartilage_y**2) < 0.3
    phantom[meniscus_mask] = 0.4  # Lower intensity for meniscus

    return phantom

# Generate and visualize phantom
phantom = generate_knee_phantom()
plt.imshow(phantom, cmap="gray")
plt.title("Synthetic Knee MRI Phantom")
plt.colorbar()
plt.show()

