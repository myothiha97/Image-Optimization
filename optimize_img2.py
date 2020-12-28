import cv2
import os
from PIL import Image
import time
start_time =time.time() 
img = cv2.imread('/home/mthk/Desktop/image-optimaztion/images/Screenshot from 2020-12-14 15-34-45.png')
img_stats = os.stat('/home/mthk/Desktop/image-optimaztion/images/Screenshot from 2020-12-14 15-34-45.png')
print(f'Original file size : {img_stats.st_size/1000} KB')
cv2.imwrite('output1.png',img , [int(cv2.IMWRITE_PNG_COMPRESSION) , 10])
out_size = os.stat('output1.png').st_size
print(f'compressed size : {out_size/1000} KB')
end_time = time.time()
total_time = end_time - start_time
total_time = time.strftime('%M:%S',time.gmtime(total_time))
print(total_time , 's')
# img = Image.open('/home/mthk/Desktop/image-optimaztion/images/Screenshot from 2020-12-14 15-34-45.png')
# img_stats = os.stat('/home/mthk/Desktop/image-optimaztion/images/Screenshot from 2020-12-14 15-34-45.png').st_size
# print(f"f'Original file size : {img_stats/1000} KB")
# img.save('out1.png',dpi = [100, 100],optimize = True , optimaztion = True,quality = 40)
# out_size = os.stat('out1.png').st_size
# print(f'compressed size : {out_size/1000} KB')



