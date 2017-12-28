import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import json

color = ('b','g','r')
idlist = ['56929c16','94462587','6d81d201','15dd8345','2a73c7e8','11581b71','bd2fd8ca','6fa53d41','32f5ee95','c335f5e7','bb1b3660','dedf2035','3b431e27','8edfadcf','601cdc58','26fb0d4f','2f881d78','87319e1c','60b72c27','7fe65b97','420de859','fd1f0c9b','9bbad755','65460dbe','9264212d','707604d3','3c98959e','5a501d33','b33ba1c3','d74b6f76','1e7ff021','43135317','de13af0f','cc6cca1f','04b03693','6cb7c7c6','93beaaaa','f5e6ceb4','c0ce2db6','9ca2cf2a','7b062647','08367f44','b8eefec7','faf2c49e','4b453753','8f7cfa57','a873532e','9c810836','d34aa573','e0323d3d','ee49f0fb','8a64ac2c','55a724b1','1c3e9901','299c9b05','5210b709','54673bc9','b8b26f06','5316efdf','92a21542','46cd533d','88b5b1aa','842784be','72da83eb','35ac7dc2','2dfb666c','d3976936','0719d5e2','cfe2ed3c','083a41f9','cc2d6324','7f9df2b0','31dc0991','6b3e62d4','29039eaa','f8c7b912','e90038aa','699105e7','606412bc','794293b5','19279980','dbd93310','66dbf620','0d276791','7bb3a881','dea041a8','010355ab']

train = pd.read_json('../static/json/train.json')
#test = pd.read_json('../static/json/test.json')

#print(test.loc[test['id'] == 'cc2d6324'])

# f = open('id.txt','w')
# for index, row in test.iterrows(): 
# 	f.write(row['id'])
# 	f.write('\n')
	
# 	print (row['id'])
# 	if (row['id'] == '3'):
# 		print('here')

# f.close()

f = open('result-sample2.txt','w')
for index, row in train.iterrows():
	#print (row['id'])
	if (row['id'] in idlist):
		

		arr = np.reshape(np.array(row['band_1']),(75,75))
		plt.imsave('img/sample2/' + row['id'] + '-' + 'band_1' + '.png', arr, cmap=plt.cm.jet)

		plt.clf()
		arr = np.reshape(np.array(row['band_2']),(75,75))
		plt.imsave('img/sample2/' + row['id'] + '-' + 'band_2' + '.png', arr, cmap=plt.cm.jet)

		#all band1
		plt.clf()
		img = cv2.imread('img/sample2/' + row['id'] + '-' + 'band_1' + '.png', 0)
		plt.hist(img.ravel(), 256,[0,256])
		plt.savefig('img/sample2/hist-' + row['id'] + '-' + 'band_1' + '.png')

		plt.clf()
		img = cv2.imread('img/sample2/' + row['id'] + '-' + 'band_1' + '.png')
		#blue = img[0,0,0]
		#print(blue)
		for i,col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[256],[0,256])
			plt.plot(histr,color = col)
			plt.xlim([0,256])
		plt.savefig('img/sample2/rgb-' + row['id'] + '-' + 'band_1' + '.png')

		#rgb - band2



		#all band2
		plt.clf()
		img = cv2.imread('img/sample2/' + row['id'] + '-' + 'band_2' + '.png', 0)
		plt.hist(img.ravel(),256,[0,256])
		plt.savefig('img/sample2/hist-' + row['id'] + '-' + 'band_2' + '.png')

		plt.clf()
		img = cv2.imread('img/sample2/' + row['id'] + '-' + 'band_2' + '.png')
		for i,col in enumerate(color):
			histr = cv2.calcHist([img],[i],None,[256],[0,256])
			plt.plot(histr,color = col)
			plt.xlim([0,256])
		plt.savefig('img/sample2/rgb-' + row['id'] + '-' + 'band_2' + '.png')



		#result
		f.write('<tr>')
		f.write('\n')

		f.write('<td>')
		f.write(row['id'])
		f.write('</td>')
		f.write('\n')

		f.write('<td><img src="img/sample2/' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample2/' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('<td>')
		if (row['is_iceberg'] == 1):
			f.write('iceberg')
		else:
			f.write('ship')
		f.write('</td>')
		f.write('\n')

		f.write('<td><img src="img/sample2/hist-' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample2/hist-' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample2/rgb-' + row['id'] + '-band_1.png"/></td>')
		f.write('\n')

		f.write('<td><img src="img/sample2/rgb-' + row['id'] + '-band_2.png"/></td>')
		f.write('\n')

		f.write('</tr>')
		f.write('\n')

# print(test[test.id == '1e7ff021'])
# print(test[test.id == '2dfb666c'])
# print(test[test.id == '8f7cfa57'])
# print(test[test.id == '11581b71'])
# print(test[test.id == '010355ab'])
# print(test[test.id == '65460dbe'])
# print(test[test.id == '1a58d98b'])
# print(test[test.id == '824277c3'])
