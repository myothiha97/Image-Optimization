import mahotas as mh
import matplotlib.pyplot as plt
import cv2
import argparse
import glob
import os
from PIL import Image
import csv
# from scipy.misc.pilutil import imread

def resized_img(url , percentage , output_url):

    # image = cv2.imread(url)
    image = mh.imread(url)
    image = image[:,:,0]
    # w , h = image.size
    width = int(image.shape[1] * percentage)
    height = int(image.shape[0] * percentage)
    dim = (width , height)
    # resized = cv2.resize(image , dim , interpolation=cv2.INTER_AREA)
    resized = mh.imresize(image , nsize=dim,order=3)
    cv2.imwrite(output_url,resized , [int(cv2.IMWRITE_PNG_COMPRESSION) , 10])
    # mh.imsave(out_url,resized)


if __name__ == "__main__":
    # urls = glob.glob('./images')
    with open('./csv_files/file_sizes_mahodaz.csv','w') as file:
        dataobj = ['Orginal_size' , 'Optimized_size','reduce_size']
        writer = csv.DictWriter(file, fieldnames=dataobj)
        writer.writeheader()

    urls = os.listdir('./images')
    for i , url in enumerate(urls):
        print(url)
        current_url = os.getcwd()
        # print(current_url)
        destination_url = os.path.join(current_url , 'images')
        org_size = os.stat(os.path.join(destination_url , url)).st_size
        # print(os.path.join(destination_url , url))
        print(org_size)
        org_size /= 1000
        org_size = float(f"{org_size:.2f}")
        os.chdir(destination_url)
        # print(os.getcwd())
        # full_url = os.path.abspath(url)
        # print(full_url)
        # os.chdir(current_url)
        out_url = os.path.join(current_url , 'out_images')
        # print(out_url,type(out_url))
        if url.endswith('.png'):
            resized_img(url , percentage=0.6,output_url = out_url + f'/optimized_{url}.png')
            optimized_size = os.stat(os.path.join(out_url,f'optimized_{url}.png')).st_size

        else:
            resized_img(url , percentage=0.6,output_url = out_url + f'/optimized_{url}.jpg')
            optimized_size = os.stat(os.path.join(out_url,f'optimized_{url}.jpg')).st_size

        optimized_size /= 1000
        optimized_size = float(f"{optimized_size:.2f}")
        reduce_size = org_size - optimized_size
        os.chdir(current_url)
        with open('./csv_files/file_sizes_mahodaz.csv','a') as file:
            dataobj = ['Orginal_size' , 'Optimized_size','reduce_size']
            writer = csv.DictWriter(file, fieldnames=dataobj)

            writer.writerow({'Orginal_size': org_size , 'Optimized_size': optimized_size , 'reduce_size': f"{reduce_size:.2f}"})