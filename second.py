import json

with open('python.json')as f:
    line = f.readline()
    tweet = json.load(line)
    print(json.dumps(tweet, indent = 4))
