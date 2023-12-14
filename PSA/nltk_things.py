from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import pos_tag
import json

try:
    with open(r'D:\PSA_MD_LABS\PSA-MD_labs-main\PSA_lab_3\lab3files\tweets.json', 'rb') as fp:
        tweets_data = json.load(fp)
except FileNotFoundError:
    print("Error: File 'tweets.json' not found.")
    tweets_data = []
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
    tweets_data = []

all_words = []
all_nouns = []
all_proper_nouns = []


custom_stopwords = ['https','rt']
stop_words = set(stopwords.words('english'))

for tweet in tweets_data:
    tweet_concept = {
        'id': tweet.get('id', None),
        'text': tweet.get('text', None),
        'created_at': tweet.get('created_at', None),
        'likes': tweet.get('likes', None),
        'retweets': tweet.get('retweets', None)
    }

    words = word_tokenize(tweet_concept['text'])

    # Filter out stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words and word.lower() not in custom_stopwords and word.isalnum()]

    all_words.extend(filtered_words)
    pos_tags = pos_tag(filtered_words)
    nouns = [word for word, pos in pos_tags if pos.startswith('N')]
    all_nouns.extend(nouns)
    proper_nouns = [word for word, pos in pos_tags if pos.startswith('NNP')]
    all_proper_nouns.extend(proper_nouns)


freq_dist = FreqDist(all_words)
noun_freq_dist = FreqDist(all_nouns)
proper_noun_freq_dist = FreqDist(all_proper_nouns)

top_words = freq_dist.most_common(10)
print("--------------------4.1------------------")
for word, frequency in top_words:
    print(f"{word}: {frequency} occurrences")

print("--------------------4.2-------------------")
top_nouns = noun_freq_dist.most_common(10)
for noun, frequency  in top_nouns:
    print(f"{noun}: {frequency} occurrences")

print("---------------------4.3------------------")
top_proper_nouns = proper_noun_freq_dist.most_common(10)
for noun, frequency  in top_proper_nouns:
    print(f"{noun}: {frequency} occurrences")
