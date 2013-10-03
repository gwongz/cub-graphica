from flask import Flask, url_for, redirect, render_template, jsonify
import json
from StringIO import StringIO

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
	return render_template('index.html')

@app.route('/index', methods = ['GET'])
def index():
	return redirect(url_for('home'))

@app.route('/portfolio', methods = ['GET'])
def portfolio():
	f = open('static/stories.json')
	data = f.read()
	json_data = json.loads(data)
	stories = json_data["stories"]

	return render_template('portfolio.html', stories=stories)



if __name__ == '__main__':
	app.run(debug = True)