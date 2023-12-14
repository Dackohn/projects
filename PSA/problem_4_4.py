from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import json
from datetime import datetime

try:
    with open(r'D:\PSA_MD_LABS\PSA-MD_labs-main\PSA_lab_3\lab3files\tweets.json', 'rb') as fp:
        tweets_data = json.load(fp)
except FileNotFoundError:
    print("Error: File 'tweets.json' not found.")
    tweets_data = []
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
    tweets_data = []


input_word = input("Enter a word to analyze: ")

dates = []
monthly_word_frequencies = {}
word_frequencies = []

for tweet in tweets_data:
    tweet_concept = {
        'text': tweet.get('text', None),
        'created_at': tweet.get('created_at', None),
    }

    words = word_tokenize(tweet_concept['text'])
    word_freq = FreqDist(words)[input_word.lower()]
    if word_freq:
        date_str = tweet_concept['created_at']
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S +0000')

        dates.append(date_obj)
        word_frequencies.append(word_freq)

        month_year = (date_obj.year, date_obj.month)

        monthly_word_frequencies[month_year] = monthly_word_frequencies.get(month_year, 0) + word_freq

formatted_keys = [f"{month}-{year}" for year, month in monthly_word_frequencies.keys()]

plt.figure(figsize=(12, 6))
plt.bar(formatted_keys, monthly_word_frequencies.values(), width=0.8, align='center', alpha=0.7)

plt.xlabel('Month and Year')
plt.ylabel(f'Frequency of "{input_word}"')
plt.title(f'Frequency of "{input_word}" over Time (1-month intervals)')
plt.tight_layout()
plt.show()
