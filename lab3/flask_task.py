from flask import Flask, jsonify
from flask import Markup
from flask import render_template
import subprocess
import sys
import time
import os
from tasks import count_pronouns
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>hello world</h1>'

@app.route('/count_pronouns')
def count():
        my_dir = '/home/ubuntu/tony-cloud-computing/lab3/data'
        os.chdir(my_dir)
        pronoun_dictionary_list = []
        han, hon, den, det, denna, denne, hen, number_of_tweets = 0, 0, 0, 0, 0, 0, 0, 0
        for file_name in os.listdir(my_dir):
                result = count_pronouns.delay(file_name)
	        while result.ready() == False:
		        time.sleep(0.1)
                pronoun_dictionary_list.append(result.result)

        for pronoun_dictionary in pronoun_dictionary_list:
	        han = han + pronoun_dictionary['han']
	        hon = hon + pronoun_dictionary['hon']
	        den = den + pronoun_dictionary['den']
	        det = det + pronoun_dictionary['det']
	        denna = denna + pronoun_dictionary['denna']
	        denne = denne + pronoun_dictionary['denne']
	        hen = hen + pronoun_dictionary['hen']
	        number_of_tweets = number_of_tweets + pronoun_dictionary['number_of_tweets']

	legend='Frequency of pronouns'
	labels=['han', 'hon', 'den', 'det','denna', 'denne', 'hen', 'number']
	values=[han, hon, den, det, denna, denne, hen, number_of_tweets]

	return render_template('chart.html', values=values, labels=labels, legend=legend)
 	
	#return '<div> han: ' + str(han) + ' hon: ' + str(hon) + ' den: ' + str(den) + ' det: ' + str(det) + ' denna: ' + str(denna) + ' denne: ' + str(denne) + ' hen: ' + str(hen) + ' number of tweet: ' + str(number_of_tweets) + ' </div>'



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
