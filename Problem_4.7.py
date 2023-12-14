import json
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import pos_tag

try:
    with open(r'lab3files\tweets.json', 'rb') as fp:
        tweets_data = json.load(fp)
except FileNotFoundError:
    print("Error: File 'tweets.json' not found.")
    tweets_data = []
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
    tweets_data = []

input_word = input("Enter a word to analyze: ")

suggestions = {}
custom_stopwords = ['https','rt']
stop_words = set(stopwords.words('english'))

for tweet in tweets_data:
    tweet_text = tweet.get('text', None)
    words = word_tokenize(tweet_text)
    filtered_words = [word for word in words if word.lower() not in stop_words and word.lower() not in custom_stopwords and word.isalnum()]
    for i in range(len(filtered_words) - 1):
        current_word = words[i].lower()

        if current_word == input_word.lower() and i < len(words) - 1:
            next_word = filtered_words[i + 1].lower()

            if next_word.isalnum() and next_word:

                if next_word in suggestions:
                    suggestions[next_word] += 1
                else:
                    suggestions[next_word] = 1


print(f"Suggestions for words following '{input_word}':")
freq_dist = FreqDist(suggestions)
top_suggestions = freq_dist.most_common(3)
for suggestion, occurrences in top_suggestions:
    print(f"{suggestion}: {occurrences} occurrences")
