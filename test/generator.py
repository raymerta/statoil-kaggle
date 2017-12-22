import json

n = 10

with open('../static/json/train.json', 'r') as f:
	train = json.load(f)
	train_length = len(train)
	train_band1_length = len(train[0]['band_1'])
	train_band2_length = len(train[0]['band_1'])

with open('train_single_' + str(n) + '.json', 'w') as outfile:
	json.dump(train[n], outfile)

# with open('../static/json/test.json', 'r') as f:
# 	test = json.load(f)
# 	test_length = len(test)
# 	test_band1_length = len(test[0]['band_1'])
# 	test_band2_length = len(test[0]['band_2'])

# with open('test_single_' + str(n) + '.json', 'w') as outfile:
# 	json.dump(test[n], outfile)