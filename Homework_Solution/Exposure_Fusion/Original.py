import cv2
import numpy as np
 
 
def readImagesAndTimes():
  
  times = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)
  
  filenames = ["Images/img_0.033.jpg", "Images/img_0.25.jpg", "Images/img_2.5.jpg", "Images/img_15.jpg"]
  images = []
  for filename in filenames:
    im = cv2.imread(filename)
    images.append(im)
  
  return images, times
 
if __name__ == '__main__':
  # Read images and exposure times
  print("Reading images ... ")
 
  images, times = readImagesAndTimes()
  
  
  # Align input images
  print("Aligning images ... ")
  alignMTB = cv2.createAlignMTB()
  alignMTB.process(images, images)
  
  # Obtain Camera Response Function (CRF)
  print("Calculating Camera Response Function (CRF) ... ")
  calibrateDebevec = cv2.createCalibrateDebevec()
  responseDebevec = calibrateDebevec.process(images, times)
  
  # Merge images into an HDR linear image
  print("Merging images into one HDR image ... ")
  mergeDebevec = cv2.createMergeDebevec()
  hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
  # Save HDR image.
  cv2.imwrite("Results/Python.hdr", hdrDebevec)
  print("saved Python.hdr ")
 