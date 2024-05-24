files={'Images/img_0.033.jpg', 'Images/img_0.25.jpg', 'Images/img_2.5.jpg', 'Images/img_15.jpg'};
expTimes=[1.0/30, 0.25, 2.5, 15.0 ];
montage(files);
hdr=makehdr(files,'RelativeExposure',expTimes./expTimes(1));
rgb=tonemap(hdr);
imshow(rgb);
hdrwrite(hdr,'Results/MATLAB.hdr');