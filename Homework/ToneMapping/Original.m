hdr_image = hdrread('HDR\office.hdr');
rgb = tonemap(hdr_image);
rgb_far=tonemapfarbman(hdr_image,'Exposure',1.5);
rgb_local=localtonemap(hdr_image,'RangeCompression',0.1);
imwrite(rgb,'Results\MATLAB\office_after.jpg');
imwrite(rgb_far,'Results\MATLAB\office_after_far.jpg');
imwrite(rgb_local,'Results\MATLAB\office_after_local.jpg');
figure
imshowpair(hdr_image,rgb,'montage')

hdr_image = hdrread('HDR\house.hdr');
rgb = tonemap(hdr_image);
rgb_far=tonemapfarbman(hdr_image,'Exposure',1.5);
rgb_local=localtonemap(hdr_image,'RangeCompression',0.1);
imwrite(rgb,'Results\MATLAB\house_after.jpg');
imwrite(rgb_far,'Results\MATLAB\house_after_far.jpg');
imwrite(rgb_local,'Results\MATLAB\house_after_local.jpg');
figure
imshowpair(hdr_image,rgb,'montage')

hdr_image = hdrread('HDR\square.hdr');
rgb = tonemap(hdr_image);
rgb_far=tonemapfarbman(hdr_image,'Exposure',1.5);
rgb_local=localtonemap(hdr_image,'RangeCompression',0.1);
imwrite(rgb,'Results\MATLAB\square_after.jpg');
imwrite(rgb_far,'Results\MATLAB\square_after_far.jpg');
imwrite(rgb_local,'Results\MATLAB\square_after_local.jpg');
figure
imshowpair(hdr_image,rgb,'montage')