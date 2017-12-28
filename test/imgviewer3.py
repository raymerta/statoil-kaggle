import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import json

color = ('b','g','r')
train = pd.read_json('../static/json/train.json')
#test = pd.read_json('../static/json/test.json')


row = train.iloc[0]

# creating image
arr = np.reshape(np.array(row['band_1']),(75,75))
plt.imsave('img/sample3/band_1' + '.png', arr, cmap=plt.cm.jet)

plt.clf()
arr = np.reshape(np.array(row['band_2']),(75,75))
plt.imsave('img/sample3/band_2' + '.png', arr, cmap=plt.cm.jet)

#all band1
plt.clf()
img = cv2.imread('img/sample3/band_1' + '.png', 0)
plt.hist(img.ravel(), 256,[0,256])
plt.savefig('img/sample3/hist-band_1' + '.png')

plt.clf()
img = cv2.imread('img/sample3/band_1' + '.png')
for i,col in enumerate(color):
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])
plt.savefig('img/sample3/rgb-band_1' + '.png')

red_img = img.copy()
red_img[:,:,0] = 0
red_img[:,:,1] = 0
cv2.imwrite('img/sample3/red-band_1' + '.png' , red_img)

green_img = img.copy()
green_img[:,:,0] = 0
green_img[:,:,2] = 0
cv2.imwrite('img/sample3/green-band_1' + '.png' , green_img)

blue_img = img.copy()
blue_img[:,:,1] = 0
blue_img[:,:,2] = 0
cv2.imwrite('img/sample3/blue-band_1' + '.png' , blue_img)

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite('img/sample3/dn-band_1' + '.png' , dst)


#all band2
plt.clf()
img = cv2.imread('img/sample3/band_2' + '.png', 0)
plt.hist(img.ravel(),256,[0,256])
plt.savefig('img/sample3/hist-band_2' + '.png')

plt.clf()
img = cv2.imread('img/sample3/band_2' + '.png')
for i,col in enumerate(color):
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])
plt.savefig('img/sample3/rgb-band_2' + '.png')

red_img = img.copy()
red_img[:,:,0] = 0
red_img[:,:,1] = 0
cv2.imwrite('img/sample3/red-band_2' + '.png' , red_img)

green_img = img.copy()
green_img[:,:,0] = 0
green_img[:,:,2] = 0
cv2.imwrite('img/sample3/green-band_2' + '.png' , green_img)

blue_img = img.copy()
blue_img[:,:,1] = 0
blue_img[:,:,2] = 0
cv2.imwrite('img/sample3/blue-band_2' + '.png' , blue_img)

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite('img/sample3/dn-band_2' + '.png' , dst)