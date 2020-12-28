import matplotlib.pyplot as plt
import cv2
from skimage import data , color 
from skimage.transform import rescale ,downscale_local_mean
import argparse
import glob
import os
from PIL import Image

def resized_img(url , percentage , output_url):

    # image = cv2.imread(url)
    image = Image.open(url)
    w , h = image.size
    width = int(w * percentage)
    height = int(h * percentage)

    dim = (width , height)
    resized = image.resize(dim ,Image.ANTIALIAS)
    # cv2.imwrite(output_url,resized , [int(cv2.IMWRITE_PNG_COMPRESSION) , 10])
    resized.save(output_url,optimize=True , quality = 60)

# image_rescale = rescale(image , 0.25 , anti_aliasing=False)

# image_rescale = downscale_local_mean(image,(2,3,3))
# cv2.imwrite('rescale_img1.png',image_rescale)
# plt.imsave('rescale_img1.png',image)

if __name__ == "__main__":
    # urls = glob.glob('./images')
    urls = os.listdir('./images')
    for i , url in enumerate(urls):
        print(url)
        current_url = os.getcwd()
        # print(current_url)
        destination_url = os.path.join(current_url , 'images')
        os.chdir(destination_url)
        # print(os.getcwd())
        # full_url = os.path.abspath(url)
        # print(full_url)
        # os.chdir(current_url)
        out_url = os.path.join(current_url , 'out_images')
        # print(out_url,type(out_url))
        if url.endswith('.png'):
            resized_img(url , percentage=0.6,output_url = out_url + f'/optimized_{url}.png')
        else:
            resized_img(url , percentage=0.6,output_url = out_url + f'/optimized_{url}.jpg')
        os.chdir(current_url)