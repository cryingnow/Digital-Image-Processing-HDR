import cv2
import numpy as np
# This file includes some typical algorithms for HDR tonemapping.


# Record the algorithms
Algorithms=["Simplest","Flimic","CryEngine","ACES","Reinhard_G","Bilateral_Filtering"]


# The simplest
def Simplest(image):
    return np.clip((np.log(1. + 5000. * image) / np.log(1. + 5000.))*255, 0, 255).astype('uint8')


# Flimic
def F(x):
    A = 0.22
    B = 0.30
    C = 0.10
    D = 0.20
    E = 0.01
    F = 0.30
    return ((x * (A * x + C * B) + D * E) / (x * (A * x + B) + D * F)) - E / F

def Flimic(image,White,adapted_lum):
    image=F(1.6*adapted_lum*image) / F(White)
    return (np.clip(image, 0, 1)*255).astype('uint8')


# CryEngine
def CryEngine(image,adapted_lum):
    # Avert it to float.
    hdr_image = image.astype(np.float32)

    image[:,:,0]=1-np.exp(-adapted_lum*hdr_image[:,:,0])
    image[:,:,1]=1-np.exp(-adapted_lum*hdr_image[:,:,1])
    image[:,:,2]=1-np.exp(-adapted_lum*hdr_image[:,:,2])
    
    return (np.clip(image, 0, 1)*255).astype('uint8')


# ACES
def ACES(image,adapted_lum):
    # Avert it to float.
    hdr_image = image.astype(np.float32)
    
    # parameter
    A=2.51
    B=0.03
    C=2.43
    D=0.59
    E=0.14
    
    hdr_image*=adapted_lum
    image=(hdr_image*(A*hdr_image+B))/(hdr_image*(C*hdr_image+D)+E)
    
    return (np.clip(image, 0, 1)*255).astype('uint8')
    

# Reinhard-Global
def Reinhard_G(image):
    # Avert it to float.
    hdr_image = image.astype(np.float32)
    
    # Parameter:Alpha as the scale factor,epsilon for avoiding zero
    alpha=0.5
    epsilon=0.000001
    
    #the log-average intensity
    adapted_lum=np.exp(np.mean(np.log(0.3*hdr_image[:,:,0]+0.59*hdr_image[:,:,1]+0.11*hdr_image[:,:,2]+epsilon)))
    
    image[:,:,0]=hdr_image[:,:,0]*alpha/adapted_lum
    image[:,:,1]=hdr_image[:,:,1]*alpha/adapted_lum
    image[:,:,2]=hdr_image[:,:,2]*alpha/adapted_lum

    return (np.clip(image, 0, 1)*255).astype('uint8')

    
# Fast Bilateral Filtering
def Bilateral_Filtering(img,Contrast):
    # Avert it to float.
    img=img.astype(np.float32)
    height, width = np.shape(img)[:2]
    
    # epsilon:Avoid the situation with 0.
    epsilon = 0.000001
    # Caculate the average intensity.
    Input_Intensity = 1/61*(20*img[:,:,0]+40*img[:,:,1]+img[:,:,2]+epsilon) 
    R = img[:,:,0]/Input_Intensity
    G = img[:,:,1]/Input_Intensity
    B = img[:,:,2]/Input_Intensity
 
    # Base,Detail,compressionFactor
    Base = cv2.bilateralFilter(np.log(Input_Intensity) , 5, 0.4, 0.02*max(height,width))
    Detail = np.log(Input_Intensity)  - Base
    compressionFactor = np.log(Contrast) / (Base.max() - Base.min())
    Output_Intensity = Base * compressionFactor + Detail
    
    img[:,:,0] = R * np.exp(Output_Intensity)
    img[:,:,1] = G * np.exp(Output_Intensity)
    img[:,:,2] = B * np.exp(Output_Intensity)
    
 
    return (np.clip(img, 0, 1)*255).astype('uint8')



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







