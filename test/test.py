from PIL import Image
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
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
	norm = mpl.colors.Normalize(vmin=band1min, vmax=band1max)
	cmap = cm.hot
	m = cm.ScalarMappable(norm=norm, cmap=cmap)

	#print m.to_rgba(x)

	band1color = []
	# assigning color value to array
	for a in train['band_1']:
		band1color.append(m.to_rgba(a))

	band1array = np.array(band1color)
	print(band1color[0])


	#print ("band_1 max value: " + str(band1max))
	#print ("band_1 min value: " + str(band1min))
	#print ("band_1 range value: " + str(band1range))



	

