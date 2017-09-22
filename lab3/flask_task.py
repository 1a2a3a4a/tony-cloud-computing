from flask import Flask, jsonify
import subprocess
import sys
from tasks import twitter
app = Flask(__name__)
@app.route('/', methods=['GET'])
def twitter_data():
    pass
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
