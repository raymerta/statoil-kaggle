import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import json

red_b1 = cv2.imread('img/sample3/red-band_1.png')
red_b2 = cv2.imread('img/sample3/red-band_2.png')
comb_red = red_b1.copy()

for i in range(75):
	for j in range(75):
		if (red_b1.item(i,j,2) == 0):
			comb_red.itemset((i,j,2),0)
		elif (red_b2.item(i,j,2) == 0):
			comb_red.itemset((i,j,2),0)
		elif (red_b1.item(i,j,2) > red_b2.item(i,j,2)):
			comb_red.itemset((i,j,2), red_b1.item(i,j,2))
		else: 
			comb_red.itemset((i,j,2), red_b2.item(i,j,2))

cv2.imwrite('img/sample3/comb_red.png' , comb_red)


blue_b1 = cv2.imread('img/sample3/blue-band_1.png')
blue_b2 = cv2.imread('img/sample3/blue-band_2.png')
comb_blue = blue_b1.copy()

for i in range(75):
	for j in range(75):
		if (blue_b1.item(i,j,0) > blue_b2.item(i,j,0)):
			comb_blue.itemset((i,j,0), blue_b1.item(i,j,0))
		elif (blue_b2.item(i,j,0) > blue_b1.item(i,j,0)):
			comb_blue.itemset((i,j,0), blue_b2.item(i,j,0))
		elif (blue_b2.item(i,j,0) == 0 and blue_b1.item(i,j,0) == 0):
			comb_blue.itemset((i,j,0), 0)
		else:
			comb_blue.itemset((i,j,0), blue_b1.item(i,j,0))

cv2.imwrite('img/sample3/comb_blue.png' , comb_blue)


green_b1 = cv2.imread('img/sample3/green-band_1.png')
green_b2 = cv2.imread('img/sample3/green-band_2.png')
comb_green = green_b1.copy()

for i in range(75):
	for j in range(75):
		if (green_b1.item(i,j,1) > green_b2.item(i,j,1)):
			comb_green.itemset((i,j,1), green_b1.item(i,j,1))
		elif (green_b2.item(i,j,1) > green_b1.item(i,j,1)):
			comb_green.itemset((i,j,1), green_b2.item(i,j,1))
		elif (green_b2.item(i,j,1) == 0 and green_b1.item(i,j,1) == 0):
			comb_green.itemset((i,j,1), 0)
		else:
			comb_green.itemset((i,j,1), green_b1.item(i,j,1))

cv2.imwrite('img/sample3/comb_green.png' , comb_green)


blue = cv2.imread('img/sample3/comb_blue.png')
green = cv2.imread('img/sample3/comb_green.png')
red = cv2.imread('img/sample3/comb_red.png')

cb = blue.copy()
for i in range(75):
	for j in range(75):
		cb.itemset((i,j,1), green.item(i,j,1))
		cb.itemset((i,j,0), blue.item(i,j,0))
		cb.itemset((i,j,2), red.item(i,j,2))

cv2.imwrite('img/sample3/comp.png' , cb)
