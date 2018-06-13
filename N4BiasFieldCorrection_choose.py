import SimpleITK as sitk

def N4():
    inputImagePath = input('Enter the path of the image : ')
    inputImage = sitk.ReadImage(inputImagePath)

    print("N4 bias correction runs.")

    # maskImage = sitk.ReadImage("06-t1c_mask.nii.gz")
    maskImage = sitk.OtsuThreshold(inputImage,0,1,200)
    maskImagePath = input('Enter the name of the mask image to be saved : ')
    sitk.WriteImage(maskImage, maskImagePath)
    print("Mask image is saved.")

    inputImage = sitk.Cast(inputImage,sitk.sitkFloat32)

    corrector = sitk.N4BiasFieldCorrectionImageFilter();

    output = corrector.Execute(inputImage,maskImage)

    outputPath = input("Enter the name of the Bias Field Corrected Image :")
    sitk.WriteImage(output,outputPath)
    print("Finished N4 Bias Field Correction.....")

if __name__=='__main__':
   N4()
