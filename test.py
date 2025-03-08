import os
import numpy as np
import matplotlib.pyplot as plt
import sigpy as sp

from dosma import preferences
from dosma.scan_sequences import QDess, CubeQuant, Cones
from dosma.tissues import FemoralCartilage
from dosma.models import IWOAIOAIUnet2DNormalized
from sigpy.plot import ImagePlot
from dosma import ImageDataFormat

fid_path = "C:/Users/cyq20/Desktop/uk/ic/y4/fyp/Py/mri-dess-pipeline/HV_data/HV1_230225/qDESS/FID"
se_path = "C:/Users/cyq20/Desktop/uk/ic/y4/fyp/Py/mri-dess-pipeline/HV_data/HV1_230225/qDESS/SE"

print(f"FID Path Exists: {os.path.exists(fid_path)}")
print(f"SE Path Exists: {os.path.exists(se_path)}")
print(f"FID Contents: {os.listdir(fid_path) if os.path.exists(fid_path) else 'Folder not found'}")
print(f"SE Contents: {os.listdir(se_path) if os.path.exists(se_path) else 'Folder not found'}")

print(f"FID Path: {fid_path}")
print(f"SE Path: {se_path}")

print("FID Contents:", os.listdir(fid_path))
print("SE Contents:", os.listdir(se_path))

qdess = QDess.from_dicom([fid_path, se_path], verbose=True)

print("QDESS successfully loaded!")
