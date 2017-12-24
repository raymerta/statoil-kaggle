import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

train = pd.read_json('../static/json/train.json')
test = pd.read_json('../static/json/test.json')

icebergs = train[train.is_iceberg==1]
ships = train[train.is_iceberg==0]

icebergs_band1 = icebergs.band_1

for index, row in icebergs.iterrows(): 
	#print(row['band_1'])
	arr = np.reshape(np.array(row['band_1']),(75,75))
	plt.imsave('img/icebergs/band1/' + str(index) + '-' + str(round(row['inc_angle'])) + '.png', arr, cmap=plt.cm.jet)

	arr = np.reshape(np.array(row['band_1']),(75,75))
	plt.imsave('img/icebergs/band1/' + str(index) + '-' + str(round(row['inc_angle'])) + '.png', arr, cmap=plt.cm.jet)




# print(icebergs_band1)

# arr = np.reshape(np.array(icebergs_band1[0]), (75,75))
# print (arr)

# for i in range(9):
#     ax = fig.add_subplot(3,3,i+1)
#     arr = np.reshape(np.array(icebergs.iloc[i,0]),(75,75))
#     ax.imshow(arr,cmap='Accent')
#plt.show()