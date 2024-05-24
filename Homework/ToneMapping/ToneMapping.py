import cv2
import numpy as np
# Finish the following funtions using different algorithms.


# Record the algorithms
Algorithms=["Simplest","Flimic","CryEngine","ACES","Reinhard_G","Bilateral_Filtering"]


# The simplest:just using exp function to fit the curve
def Simplest(image):
    
    return 


# Flimic
def F(x):
   
    return 

def Flimic(image,White,adapted_lum):
    
    return 


# CryEngine
def CryEngine(image,adapted_lum):
    
    return 


# ACES
def ACES(image,adapted_lum):

    return 
    

# Reinhard-Global
def Reinhard_G(image):

    return 

    
# Fast Bilateral Filtering
def Bilateral_Filtering(img,Contrast):
   
    return 



# Summary of all algorithms
def All_Solutions(image,index):
    if index==0:
        return Simplest(image)
    if index==1:
        return Flimic(image,11.2,15)
    if index==2:
        return CryEngine(image,10)
    if index==3:
        return ACES(image,0.8)
    if index==4:
        return Reinhard_G(image)
    if index==5:
        return Bilateral_Filtering(image,5)
    
    
# Read the test images.
hdr_office=cv2.imread('HDR\office.hdr',cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)
hdr_house=cv2.imread('HDR\house.hdr',cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)
hdr_square=cv2.imread('HDR\square.hdr',cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)


# Test 3 HDR images using each algorithm.
for i in range(0,6):
    ldr_office=All_Solutions(hdr_office,i)
    ldr_house=All_Solutions(hdr_house,i)
    ldr_square=All_Solutions(hdr_square,i)
    cv2.imwrite("Results\\" +Algorithms[i]+ "\\office.jpg",ldr_office)
    cv2.imwrite("Results\\" +Algorithms[i]+ "\\house.jpg",ldr_house)
    cv2.imwrite("Results\\" +Algorithms[i]+ "\\square.jpg",ldr_square)
    print("Algorithm "+ Algorithms[i] +" succeeded.")







