from dosma import ImagingData, ImagingModality

# Load an MRI scan (replace with your actual file path)
mri_image = ImagingData.from_path("knee_mri.nii.gz", modality=ImagingModality.MRI)

# Print information
print(mri_image)

