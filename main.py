import numpy as np
import matplotlib.pyplot as plt
import imutils 
import cv2  
from matplotlib import pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

path = '/content/drive/MyDrive/PIM/'
verticalBars = imread(path+'verticalBars.png')

def fourier(img):
  dark_image_grey = rgb2gray(img)
  #plt.figure(num=None, figsize=(8, 6), dpi=80)
  
  dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(dark_image_grey))
  #plt.figure(num=None, figsize=(8, 6), dpi=80)
  
  fig, ax = plt.subplots(1,2,figsize=(15,15))
  ax[0].imshow(dark_image_grey, cmap='gray')
  ax[1].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
  
  
  
def transladar(image, horizontal=0, vertical=0):
  altura, largura = image.shape[:2]
  deslocamento = np.float32([[1, 0, horizontal], [0, 1, vertical]])
  deslocado = cv2.warpAffine(image, deslocamento, (largura, altura))
  #plt.imshow(deslocado)
  #plt.show()
  return deslocado

vert = 10 # Transladar para Verticalmente
hori = 10 # Transladar para Horizontamente

#fourier(transladar(verticalBars, vert, hori))

fourier(transladar(verticalBars, 0, 0))
for im in range(6):
  fourier(transladar(verticalBars, vert, hori))
  vert += 15 
  hori += 15 
