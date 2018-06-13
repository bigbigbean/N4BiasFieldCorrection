import SimpleITK as sitk

def N4():
    print("N4 bias correction runs.")
    inputImage = sitk.ReadImage("06-t1c.nii.gz")
    # maskImage = sitk.ReadImage("06-t1c_mask.nii.gz")
    maskImage = sitk.OtsuThreshold(inputImage,0,1,200)
    sitk.WriteImage(maskImage, "06-t1c_mask3.nii.gz")

    inputImage = sitk.Cast(inputImage,sitk.sitkFloat32)

    corrector = sitk.N4BiasFieldCorrectionImageFilter();

    output = corrector.Execute(inputImage,maskImage)
    sitk.WriteImage(output,"06-t1c_output3.nii.gz")
    print("Finished N4 Bias Field Correction.....")

if __name__=='__main__':
   N4()
