from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import OrderedDict
import json

try:
    with open(r'D:\PSA_MD_LABS\PSA-MD_labs-main\PSA_lab_3\lab3files\tweets.json', 'r', encoding='utf-8') as fp:
        tweets_data = json.load(fp)
except FileNotFoundError:
    print("Error: File 'tweets.json' not found.")
    tweets_data = []
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
    tweets_data = []
word_scores = {}

with open('D:\PSA_MD_LABS\PSA-MD_labs-main\PSA_lab_3\lab3files\AFINN-111.txt', 'r') as file:
    for line in file:
        word, score = line.strip().split('\t')
        score = int(score)
        word_scores[word] = score

all_hashtags = []
custom_stopwords = ['https', 'rt', 'http']
stop_words = set(stopwords.words('english'))
hashtags = {}

tweets_value = {}

for tweet in tweets_data:
    tweet_concept = {
        'id': tweet.get('id', None),
        'text': tweet.get('text', None),
        'created_at': tweet.get('created_at', None),
        'likes': tweet.get('likes', None),
        'retweets': tweet.get('retweets', None)
    }

    words = word_tokenize(tweet_concept['text'])
    id = tweet_concept['id']
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in custom_stopwords]
    for word in filtered_words:
        if word in word_scores:
            if id in tweets_value:
                tweets_value[id] += word_scores[word]
            else:
                tweets_value[id] = word_scores[word]


sorted_tweets = dict(sorted(tweets_value.items(), key=lambda item: item[1], reverse=True))
print("-----------Most positive tweets--------------------")
for i, (id, value) in enumerate(sorted_tweets.items()):
    print(f"{id}: {value}")
    i +=1
    if i == 9:
        break
sorted_tweets = dict(reversed(list(sorted_tweets.items())))
print("-----------Most negative tweets--------------------")
for i, (id, value) in enumerate(sorted_tweets.items()):
    print(f"{id}: {value}")
    i +=1
    if i == 9:
        break