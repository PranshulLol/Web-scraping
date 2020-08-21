import json
from nltk.tokenize import word_tokenize 

with open('python.json', 'r') as f:
    line = f.readline()
    tweet = json.loads(line)
    print(json.dumps(tweet, indent=4))
