import json

n = 35

with open('../static/json/train.json', 'r') as f:
	train = json.load(f)

with open('train_single_' + str(n) + '.json', 'w') as outfile:
	json.dump(train[n], outfile)

# with open('../static/json/test.json', 'r') as f:
# 	test = json.load(f)
# 	test_length = len(test)
# 	test_band1_length = len(test[0]['band_1'])
# 	test_band2_length = len(test[0]['band_2'])

# with open('test_single_' + str(n) + '.json', 'w') as outfile:
# 	json.dump(test[n], outfile)