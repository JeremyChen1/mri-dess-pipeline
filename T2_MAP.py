import os
import numpy as np
import matplotlib.pyplot as plt
from dosma import ImageDataFormat
from dosma.scan_sequences import QDess
from dosma.tissues import FemoralCartilage

# Define your data path
base_path = os.path.join("C:\\Users", "cyq20", "Desktop", "uk", "ic", "y4", "fyp", "Py", "mri-dess-pipeline", "HV_data", "HV1_230225")
qdess_dicom = os.path.join(base_path)

# Load the qDESS scan
qdess = QDess.from_dicom(qdess_dicom, verbose=True)

# Define a femoral cartilage object
fc = FemoralCartilage()

# Compute T2 mapping while suppressing fat and fluid regions
t2map = qdess.generate_t2_map(fc, suppress_fat=True, suppress_fluid=True)

# Clip the T2 values to a reasonable range [0, 80 ms]
t2map.volumetric_map = np.clip(t2map.volumetric_map, 0, 80)

# Visualize the T2 map
plt.imshow(t2map.volumetric_map.A[:, :, 34])
plt.colorbar()
plt.title("T2 Map of Knee Cartilage")
plt.show()

# Save scan data (DICOM format)
qdess.save("./results/qdess", save_custom=True, image_data_format=ImageDataFormat.dicom)

