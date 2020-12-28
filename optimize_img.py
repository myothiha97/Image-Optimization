from PIL import Image
import pyguetzli
import cv2
import numpy as np
import os
import time

start_time = time.time()
org_img = '/home/mthk/Desktop/image-optimaztion/images/Screenshot from 2020-10-15 23-10-17.jpg'
img_stats = os.stat(org_img)
print(f'Original file size : {img_stats.st_size/1000} KB')
# convert_img  = Image.open(org_img)
# convert_img.save('./images/1.jpg')

# convert_img = cv2.imread(org_img)
# cv2.imwrite('./images/1.jpg',convert_img)
# file = open('./images/1.jpg','rb').read()
# opt_img = pyguetzli.process_jpeg_bytes(file , quality= 50)
img = Image.open(org_img)

opt_img = pyguetzli.process_pil_image(img, quality=80)
output = open('opt_img1.jpg','wb')
output.write(opt_img)

out_stats = os.stat('opt_img1.jpg').st_size
print(f"Compressed image size : {out_stats/1000} KB")
end_time = time.time()
total_time = round(end_time - start_time)

if total_time >= 60:
    time_interval = (total_time/60)
    print(f'execution time -----------> {time_interval:.2f} min')
else:
    print(f'execution time -----------> {total_time} sec')