from PIL import Image
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json

w, h = 75, 75
data = np.zeros((h, w, 3), dtype=np.uint8)
# data[30, 30] = [255, 0, 0]
# img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()




with open('train_single.json', 'r') as f:
	train = json.load(f)
	band1max = max(train['band_1'])
	band1min = min(train['band_1'])
	band1range = band1max - band1min

	# trying to assign color to the array
	#print (cm.hot(0.3))

	norm = mpl.colors.Normalize(vmin=-20, vmax=10)
	cmap = cm.hot
	m = cm.ScalarMappable(norm=norm, cmap=cmap)

	# assigning color value to array
	band1color = []
	for a in train['band_1']:
		decval = (a - band1min) / band1range
		torgb = int(decval * 255)
		band1color.append([torgb, torgb, torgb])

	for a in range(w):
		for b in range(h): 
			data[a,b] = band1color[a + b]

	img = Image.fromarray(data, 'RGB')
	img.save('pic0.png')
	img.show()

	#print ("band_1 max value: " + str(band1max))
	#print ("band_1 min value: " + str(band1min))
	#print ("band_1 range value: " + str(band1range))



	

