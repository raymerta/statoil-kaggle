import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import json

idlist = ['cc2d6324','1e7ff021','2dfb666c','8f7cfa57','11581b71','010355ab','65460dbe','1a58d98b','824277c3']

train = pd.read_json('../static/json/train.json')

f = open('result-comp.txt','w')
for index, row in train.iterrows():
	if (row['id'] in idlist):

		#create images
		arr = np.reshape(np.array(row['band_1']),(75,75))
		plt.imsave('img/comp/' + row['id'] + '-band_1' + '.png', arr, cmap=plt.cm.jet)

		plt.clf()
		arr = np.reshape(np.array(row['band_2']),(75,75))
		plt.imsave('img/comp/' + row['id'] + '-band_2' + '.png', arr, cmap=plt.cm.jet)

		#all band1
		plt.clf()
		img = cv2.imread('img/comp/' + row['id'] + '-band_1' + '.png', 0)
		plt.hist(img.ravel(), 256,[0,256])
		plt.savefig('img/comp/' + row['id'] + '-hist-band_1' + '.png')

		plt.clf()
		img = cv2.imread('img/comp/' + row['id'] + '-band_1' + '.png')

		red_img = img.copy()
		red_img[:,:,0] = 0
		red_img[:,:,1] = 0
		cv2.imwrite('img/comp/' + row['id'] + '-red-band_1' + '.png' , red_img)

		green_img = img.copy()
		green_img[:,:,0] = 0
		green_img[:,:,2] = 0
		cv2.imwrite('img/comp/' + row['id'] + '-green-band_1' + '.png' , green_img)

		blue_img = img.copy()
		blue_img[:,:,1] = 0
		blue_img[:,:,2] = 0
		cv2.imwrite('img/comp/' + row['id'] + '-blue-band_1' + '.png' , blue_img)

		dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
		cv2.imwrite('img/comp/' + row['id'] + '-dn-band_1' + '.png' , dst)


		#all band2
		plt.clf()
		img = cv2.imread('img/comp/' + row['id'] + '-band_2' + '.png', 0)
		plt.hist(img.ravel(),256,[0,256])
		plt.savefig('img/comp/' + row['id'] + '-hist-band_2' + '.png')

		plt.clf()
		img = cv2.imread('img/comp/' + row['id'] + '-band_2' + '.png')

		red_img = img.copy()
		red_img[:,:,0] = 0
		red_img[:,:,1] = 0
		cv2.imwrite('img/comp/' + row['id'] + '-red-band_2' + '.png' , red_img)

		green_img = img.copy()
		green_img[:,:,0] = 0
		green_img[:,:,2] = 0
		cv2.imwrite('img/comp/' + row['id'] + '-green-band_2' + '.png' , green_img)

		blue_img = img.copy()
		blue_img[:,:,1] = 0
		blue_img[:,:,2] = 0
		cv2.imwrite('img/comp/' + row['id'] + '-blue-band_2' + '.png' , blue_img)

		dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
		cv2.imwrite('img/comp/' + row['id'] + '-dn-band_2' + '.png' , dst)		

		red_b1 = cv2.imread('img/comp/' + row['id'] + '-red-band_1.png')
		red_b2 = cv2.imread('img/comp/' + row['id'] + '-red-band_2.png')
		comb_red = red_b1.copy()

		for i in range(75):
			for j in range(75):
				if (red_b1.item(i,j,2) == 0):
					comb_red.itemset((i,j,2),0)
				elif (red_b2.item(i,j,2) == 0):
					comb_red.itemset((i,j,2),0)
				elif (red_b1.item(i,j,2) > red_b2.item(i,j,2)):
					comb_red.itemset((i,j,2), red_b2.item(i,j,2))
				else: 
					comb_red.itemset((i,j,2), red_b1.item(i,j,2))

		cv2.imwrite('img/comp/' + row['id'] + '-comb_red.png' , comb_red)


		blue_b1 = cv2.imread('img/comp/' + row['id'] + '-blue-band_1.png')
		blue_b2 = cv2.imread('img/comp/' + row['id'] + '-blue-band_2.png')
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

		cv2.imwrite('img/comp/' + row['id'] + '-comb_blue.png' , comb_blue)


		green_b1 = cv2.imread('img/comp/' + row['id'] + '-green-band_1.png')
		green_b2 = cv2.imread('img/comp/' + row['id'] + '-green-band_2.png')
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

		cv2.imwrite('img/comp/' + row['id'] + '-comb_green.png' , comb_green)


		blue = cv2.imread('img/comp/' + row['id'] + '-comb_blue.png')
		green = cv2.imread('img/comp/' + row['id'] + '-comb_green.png')
		red = cv2.imread('img/comp/' + row['id'] + '-comb_red.png')

		cb = blue.copy()
		for i in range(75):
			for j in range(75):
				cb.itemset((i,j,1), green.item(i,j,1))
				cb.itemset((i,j,0), blue.item(i,j,0))
				cb.itemset((i,j,2), red.item(i,j,2))

		cv2.imwrite('img/comp/' + row['id'] + '-comp.png' , cb)


		#result
		f.write('<tr>')
		f.write('\n')

		f.write('<td>')
		f.write(row['id'])
		f.write('</td>')
		f.write('\n')

		f.write('<td><img src="img/comp/' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/comp/' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/comp/' + row['id'] + '-comb_blue.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/comp/' + row['id'] + '-comb_green.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/comp/' + row['id'] + '-comb_red.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/comp/' + row['id'] + '-comp.png"/></td>')
		f.write('\n')

		f.write('<td>')
		if (row['is_iceberg'] == 1):
			f.write('iceberg')
		else:
			f.write('ship')
		f.write('</td>')
		f.write('\n')

		f.write('<td>')
		f.write(str(row['inc_angle']))
		f.write('</td>')
		f.write('\n')


		f.write('</tr>')
		f.write('\n')