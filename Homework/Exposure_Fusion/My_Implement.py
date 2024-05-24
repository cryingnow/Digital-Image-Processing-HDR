import os
import random
import cv2
import numpy as np 

# Load the images(lists) and their exposure times.
def load(path_test):
    filenames = []
    exposure_times = []
    f = open(os.path.join(path_test, 'image_list.txt'))
    for line in f:
        if (line[0] == '#'):
            continue
        # (filename, exposure, *rest) = line.split()
        (filename, exposure) = line.split()
        filenames += [os.path.join(path_test,filename)]
        # exposure_times += [math.log(float(exposure),2)]
        exposure_times += [float(exposure)]
    return filenames, exposure_times

# Read the image lists
def read(path_list):
    shape = cv2.imread(path_list[0]).shape

    stack = np.zeros((len(path_list), shape[0], shape[1], shape[2]))
    for i in path_list:
        im = cv2.imread(i)
        stack[path_list.index(i), :, :, :] = im
    return stack

# Calculate the weight of intensity
def weight(I):
    
    return 

# Get the intensity from the stack
def sample_intensity(stack):
    
    return 

# Estimate the Camera Response Function curve
def estimate_curve(sample, exps, l):

    return 


# Recover the radiance by linear.
def computeRadiance(stack, exps, curve):

    return 





list_file, exps = load("Images")
stack = read(list_file)

num_channels = stack.shape[-1]
hdr_img = np.zeros(stack[0].shape, dtype=np.float64)

for c in range(num_channels):
    layer_stack = [img[:,:,c] for img in stack]
        
    sample = sample_intensity(layer_stack)

    curve = estimate_curve(sample, exps, 100.)

    img_rad = computeRadiance(np.array(layer_stack), exps, curve)

    hdr_img[:,:, c] = cv2.normalize(img_rad, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

cv2.imwrite(os.path.join("Results", 'My_Implement.hdr'), hdr_img)