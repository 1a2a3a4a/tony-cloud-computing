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
                    text_tweet.append(json.loads(line)['text'].lower())
                except:
                    print 'error'
    
    han = 0
    hon = 0
    den = 0
    det = 0
    denna = 0
    denne = 0
    hen = 0
    pronoun_dictionary = {}
    pronoun_dictionary['han'] = han
    pronoun_dictionary['hon'] = hon
    pronoun_dictionary['den'] = den
    pronoun_dictionary['det'] = det
    pronoun_dictionary['denna'] = denna
    pronoun_dictionary['denne'] = denne
    pronoun_dictionary['hen'] = hen
    
    
    unique_tweets = set(text_tweet)
    number_of_unique = len(unique_tweets)
    pronoun_dictionary['number_of_tweets'] = len(text_tweet)
    
    for tweet in unique_tweets:
        if 'han' in tweet:
            pronoun_dictionary['han'] += 1
        if 'hon' in tweet:
            pronoun_dictionary['hon'] += 1 
        if 'den' in tweet:
            pronoun_dictionary['den'] += 1 
        if 'det' in tweet:
            pronoun_dictionary['det'] += 1 
        if 'denna' in tweet:
            pronoun_dictionary['denna'] += 1
        if 'denne' in tweet:
            pronoun_dictionary['denne'] += 1
        if 'hen' in tweet:
            pronoun_dictionary['hen'] += 1 
        
    return pronoun_dictionary