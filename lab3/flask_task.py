from flask import Flask, jsonify
import subprocess
import sys
from tasks import count_pronouns
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>hello world</h1>'

@app.route('/count_pronouns', methods=['GET'])
def count():
	result = count_pronouns.delay()
	while not result.ready():
		pass
	return result.result

if __name__ == '__main__':
    app.run(debug=True)
    
