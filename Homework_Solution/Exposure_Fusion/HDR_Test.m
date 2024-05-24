hdr_image = hdrread('Results/MATLAB.hdr');
rgb = tonemap(hdr_image);
imwrite(rgb,'Results/MATLAB.jpg');
figure
imshowpair(hdr_image,rgb,'montage')

hdr_image = hdrread('Results/Python.hdr');
rgb = tonemap(hdr_image);
imwrite(rgb,'Results/Python.jpg');
figure
imshowpair(hdr_image,rgb,'montage')

hdr_image = hdrread('Results/My_Implement.hdr');
rgb = tonemap(hdr_image);
imwrite(rgb,'Results/My_Implment.jpg');
figure
imshowpair(hdr_image,rgb,'montage')