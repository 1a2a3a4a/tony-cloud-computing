from flask import Flask, jsonify
import subprocess
import sys
import time
from tasks import count_pronouns
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>hello world</h1>'

@app.route('/count_pronouns', methods=['GET'])
def count():
	result = count_pronouns.delay()
	while result.ready() == False:
		time.sleep(0.1)
	return '<h1>' + result.result + '<h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
