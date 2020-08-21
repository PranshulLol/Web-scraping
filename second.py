import json
from nltk.tokenize import word_tokenize 
# nltk.download('punkt')
# with open('python.json', 'r') as f:
#     line = f.readline()
#     tweet = json.loads(line)
#     print(json.dumps(tweet, indent=4))
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(tweet))

