import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import json

color = ('b','g','r')
train = pd.read_json('../static/json/train.json')
#test = pd.read_json('../static/json/test.json')

f = open('result-sample.txt','w')
for index, row in train.iterrows():
	#print (row['id'])
	if (row['id'] == 'cc2d6324' or 
		row['id'] == '1e7ff021' or
		row['id'] == '2dfb666c' or 
		row['id'] == '8f7cfa57' or 
		row['id'] == '11581b71' or 
		row['id'] == '010355ab' or 
		row['id'] == '65460dbe' or 
		row['id'] == '1a58d98b' or
		row['id'] == '824277c3'  ):
		

		arr = np.reshape(np.array(row['band_1']),(75,75))
		plt.imsave('img/sample/' + row['id'] + '-' + 'band_1' + '.png', arr, cmap=plt.cm.jet)

		plt.clf()
		arr = np.reshape(np.array(row['band_2']),(75,75))
		plt.imsave('img/sample/' + row['id'] + '-' + 'band_2' + '.png', arr, cmap=plt.cm.jet)

		#all band1
		plt.clf()
		img = cv2.imread('img/sample/' + row['id'] + '-' + 'band_1' + '.png', 0)
		plt.hist(img.ravel(), 256,[0,256])
		plt.savefig('img/sample/hist-' + row['id'] + '-' + 'band_1' + '.png')

		plt.clf()
		img = cv2.imread('img/sample/' + row['id'] + '-' + 'band_1' + '.png')
		for i,col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[256],[0,256])
			plt.plot(histr,color = col)
			plt.xlim([0,256])
		plt.savefig('img/sample/rgb-' + row['id'] + '-' + 'band_1' + '.png')

		red_img = img.copy()
		red_img[:,:,0] = 0
		red_img[:,:,1] = 0
		cv2.imwrite('img/sample/red-'  + row['id'] + '-' + 'band_1' + '.png' , red_img)

		green_img = img.copy()
		green_img[:,:,0] = 0
		green_img[:,:,2] = 0
		cv2.imwrite('img/sample/green-'  + row['id'] + '-' + 'band_1' + '.png' , green_img)

		blue_img = img.copy()
		blue_img[:,:,1] = 0
		blue_img[:,:,2] = 0
		cv2.imwrite('img/sample/blue-'  + row['id'] + '-' + 'band_1' + '.png' , blue_img)

		dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
		cv2.imwrite('img/sample/dn-'  + row['id'] + '-' + 'band_1' + '.png' , dst)


		#all band2
		plt.clf()
		img = cv2.imread('img/sample/' + row['id'] + '-' + 'band_2' + '.png', 0)
		plt.hist(img.ravel(),256,[0,256])
		plt.savefig('img/sample/hist-' + row['id'] + '-' + 'band_2' + '.png')

		plt.clf()
		img = cv2.imread('img/sample/' + row['id'] + '-' + 'band_2' + '.png')
		for i,col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[256],[0,256])
			plt.plot(histr,color = col)
			plt.xlim([0,256])
		plt.savefig('img/sample/rgb-' + row['id'] + '-' + 'band_2' + '.png')

		red_img = img.copy()
		red_img[:,:,0] = 0
		red_img[:,:,1] = 0
		cv2.imwrite('img/sample/red-'  + row['id'] + '-' + 'band_2' + '.png' , red_img)

		green_img = img.copy()
		green_img[:,:,0] = 0
		green_img[:,:,2] = 0
		cv2.imwrite('img/sample/green-'  + row['id'] + '-' + 'band_2' + '.png' , green_img)

		blue_img = img.copy()
		blue_img[:,:,1] = 0
		blue_img[:,:,2] = 0
		cv2.imwrite('img/sample/blue-'  + row['id'] + '-' + 'band_2' + '.png' , blue_img)

		dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
		cv2.imwrite('img/sample/dn-'  + row['id'] + '-' + 'band_2' + '.png' , dst)



		#result
		f.write('<tr>')
		f.write('\n')

		f.write('<td>')
		f.write(row['id'])
		f.write('</td>')
		f.write('\n')

		f.write('<td><img src="img/sample/' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		

		# f.write('<td><img src="img/sample/hist-' + row['id'] + '-band_1.png"/></td>')
		# f.write('\n')

		# f.write('<td><img src="img/sample/hist-' + row['id'] + '-band_2.png"/></td>')
		# f.write('\n')

		# f.write('<td><img src="img/sample/rgb-' + row['id'] + '-band_1.png"/></td>')
		# f.write('\n')

		# f.write('<td><img src="img/sample/rgb-' + row['id'] + '-band_2.png"/></td>')
		# f.write('\n')

		f.write('<td><img src="img/sample/red-' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/red-' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/green-' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/green-' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/blue-' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/blue-' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/dn-' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample/dn-' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')



		f.write('<td>')
		if (row['is_iceberg'] == 1):
			f.write('iceberg')
		else:
			f.write('ship')
		f.write('</td>')
		f.write('\n')

		f.write('</tr>')
		f.write('\n')

