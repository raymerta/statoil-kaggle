from flask import Flask, render_template, jsonify, request, send_from_directory, url_for
import json, requests

app = Flask(__name__)


@app.route('/')
def index():

	#print("do request")

	#url = request.base_url + 'data/json/train.json'
	#resp = requests.get(url=url)
	#data = json.loads(resp.text)

	#print(data[0])

	with open('static/json/train.json', 'r') as f:
		train = json.load(f)
		train_length = len(train)

	with open('static/json/test.json', 'r') as f:
		test = json.load(f)
		test_length = len(test)

	#print (data[0])

	return render_template('index.html', train = train, test = test, train_length = train_length, test_length = test_length)

@app.route('/data/<path:path>')
def send_json(path):
    return send_from_directory('static', path)