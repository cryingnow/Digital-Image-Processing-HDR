import cv2


#office.hdr
hdrDebevec=cv2.imread('HDR\office.hdr',cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)

# Drago's method
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3 * ldrDrago
cv2.imwrite("Results\Python\office_Drago.jpg", ldrDrago * 255)

# Reinhard's method
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
ldrReinhard = tonemapReinhard.process(hdrDebevec)
cv2.imwrite("Results\Python\office_Reinhard.jpg", ldrReinhard * 255)

# Mantiuk's method
tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
ldrMantiuk = 3 * ldrMantiuk
cv2.imwrite("Results\Python\office_Mantiuk.jpg", ldrMantiuk * 255)




#house.hdr
hdrDebevec=cv2.imread('HDR\house.hdr',cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)

# Drago's method
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3 * ldrDrago
cv2.imwrite("Results\Python\house_Drago.jpg", ldrDrago * 255)

# Reinhard's method
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
ldrReinhard = tonemapReinhard.process(hdrDebevec)
cv2.imwrite("Results\Python\house_Reinhard.jpg", ldrReinhard * 255)

# Mantiuk's method
tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
ldrMantiuk = 3 * ldrMantiuk
cv2.imwrite("Results\Python\house_Mantiuk.jpg", ldrMantiuk * 255)






#square.hdr
hdrDebevec=cv2.imread('HDR\square.hdr',cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)

# Drago's method
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3 * ldrDrago
cv2.imwrite("Results\Python\square_Drago.jpg", ldrDrago * 255)

# Reinhard's method
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
ldrReinhard = tonemapReinhard.process(hdrDebevec)
cv2.imwrite("Results\Python\square_Reinhard.jpg", ldrReinhard * 255)

# Mantiuk's method
tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
ldrMantiuk = 3 * ldrMantiuk
cv2.imwrite("Results\Python\square_Mantiuk.jpg", ldrMantiuk * 255)