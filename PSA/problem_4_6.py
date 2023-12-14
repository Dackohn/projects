from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
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

all_proposed_words = []
input_begining = input("Write the beggining of a word: ")


custom_stopwords = ['https','rt']
stop_words = set(stopwords.words('english'))

for tweet in tweets_data:
    tweet_concept = {
        'text': tweet.get('text', None),
    }

    words = word_tokenize(tweet_concept['text'])
    filtered_words = [word for word in words if word.lower() not in stop_words and word.lower() not in custom_stopwords and word.isalnum()]
    proposed_words = [word for word in filtered_words if word.startswith(input_begining.lower())]
    all_proposed_words.extend(proposed_words)


proposed_words_freq_dist = FreqDist(all_proposed_words)
top_proposed_words = proposed_words_freq_dist.most_common(3)
print("Proposed words:")
for word, frequency in top_proposed_words:
    print(f"{word} : {frequency} occurences")
