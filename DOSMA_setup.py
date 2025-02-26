import os
from dosma import ImagingData, ImagingModality
from dosma.scan_sequences import QDess, CubeQuant, Cones

# Define paths
data_path = "HV_data/HV1_230225"
qdess_dicom = os.path.join(data_path, "qDESS")
cubequant_dicom = os.path.join(data_path, "CubeQuant")
cones_dicom = os.path.join(data_path, "Cones")

# Convert DICOM to NIfTI (if needed)
qdess_nifti = "HV_data/HV1_230225/qDESS.nii.gz"
cubequant_nifti = "HV_data/HV1_230225/CubeQuant.nii.gz"
cones_nifti = "HV_data/HV1_230225/Cones.nii.gz"

if not os.path.exists(qdess_nifti):
    qdess = ImagingData.from_path(qdess_dicom, modality=ImagingModality.MRI)
    qdess.to_nifti(qdess_nifti)

if not os.path.exists(cubequant_nifti):
    cubequant = ImagingData.from_path(cubequant_dicom, modality=ImagingModality.MRI)
    cubequant.to_nifti(cubequant_nifti)

if not os.path.exists(cones_nifti):
    cones = ImagingData.from_path(cones_dicom, modality=ImagingModality.MRI)
    cones.to_nifti(cones_nifti)

# Load MRI sequences
qdess = QDess.from_nifti(qdess_nifti)
cubequant = CubeQuant.from_nifti(cubequant_nifti)
cones = Cones.from_nifti(cones_nifti)

# Align CubeQuant and Cones to qDESS
cubequant.interregister(qdess.volumes[0])
cones.interregister(qdess.volumes[0])

print("MRI Data Setup Complete!")
