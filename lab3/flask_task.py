from flask import Flask, jsonify
from flask import Markup
from flask import render_template
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
	pronoun_dictionary = result.result

	han = pronoun_dictionary['han']
	hon = pronoun_dictionary['hon']
	den = pronoun_dictionary['den']
	det = pronoun_dictionary['det']
	denna = pronoun_dictionary['denna']
	denne = pronoun_dictionary['denne']
	hen= pronoun_dictionary['hen']
	number_of_tweets = pronoun_dictionary['number_of_tweets']

	values=['han', 'hon', 'den', 'det','denna', 'denne', 'hen']
	labels=[han, hon, den, det, denna, denne, hen]

	return render_template('chart.html', values=values, labels=labels)
 	
	#return '<div> han: ' + str(han) + ' hon: ' + str(hon) + ' den: ' + str(den) + ' det: ' + str(det) + ' denna: ' + str(denna) + ' denne: ' + str(denne) + ' hen: ' + str(hen) + ' number of tweet: ' + str(number_of_tweets) + ' </div>'



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
