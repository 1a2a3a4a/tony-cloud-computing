from celery import Celery
import json
app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y

@app.task
def count_pronouns():
    file_path = 'data03'
    text_tweet = []

    with open(file_path) as f:
        for line in f:
            if line[0] == '{':
                try:
                    text_tweet.append(json.loads(line)['text'].lower()
                except:
                    print 'error'
    
    han = 0
    hon = 0
    den = 0
    det = 0
    denna = 0
    denne = 0
    hen = 0

    unique_tweets = set(text_tweet)
    number_of_unique = len(unique_tweets)
    
    for tweet in unique_tweets:
        if 'han' in tweet:
            han += 1
        if 'hon' in tweet:
            hon += 1
        if 'den' in tweet:
            den += 1
        if 'det' in tweet:
            det += 1
        if 'denna' in tweet:
            denna += 1
        if 'denne' in tweet:
            denne += 1
        if 'hen' in tweet:
            hen += 1
    print han, hon, den, det, denna, denne, hen, number_of_unique
