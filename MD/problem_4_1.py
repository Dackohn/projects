from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
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

all_hashtags = []
custom_stopwords = ['https', 'rt', 'http']
stop_words = set(stopwords.words('english'))
hashtags = {}

for tweet in tweets_data:
    tweet_concept = {
        'id': tweet.get('id', None),
        'text': tweet.get('text', None),
        'created_at': tweet.get('created_at', None),
        'likes': tweet.get('likes', None),
        'retweets': tweet.get('retweets', None)
    }

    words = word_tokenize(tweet_concept['text'])
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in custom_stopwords]

    i = 0
    while i < len(filtered_words) - 1:
        if filtered_words[i] == '#':
            hashtag = filtered_words[i] + filtered_words[i + 1]
            if hashtag in hashtags:
                hashtags[hashtag] += 1
            else:
                hashtags[hashtag] = 1
            i += 2  # Move to the next word after the hashtag
        else:
            i += 1
sorted_hash = dict(sorted(hashtags.items(), key=lambda item: item[1], reverse=True))
for i ,(hash, occur) in enumerate(sorted_hash.items()):
    print(f"{hash}: {occur} occurrences")
    if i == 9:
        break
    i += 1
