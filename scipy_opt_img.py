import scipy
import cv2
# from scipy import misc
import imageio
# img = cv2.imread('/home/mthk/Desktop/image-optimaztion/images/aldino-hartan-putra-YqN0mzwVsz0-unsplash.jpg')
# img = misc.imread('/home/mthk/Desktop/image-optimaztion/images/aldino-hartan-putra-YqN0mzwVsz0-unsplash.jpg')
img = imageio.imread('/home/mthk/Desktop/image-optimaztion/images/aldino-hartan-putra-YqN0mzwVsz0-unsplash.jpg')

height = int(img.shape[0] * 0.6)
width = int(img.shape[1] * 0.6)
dim = (width , height)
# resized = scipy.misc.imresize(img , dim)
imageio.imwrite('imageio1.jpg',img)
misc.imsave('scipy1.jpg',resized)