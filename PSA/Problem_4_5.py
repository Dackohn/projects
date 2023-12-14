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


custom_stopwords = ['https','rt' , 'http']
stop_words = set(stopwords.words('english'))

word_like = {}
word_retweet = {}
all_nouns = []

for tweet in tweets_data:
    tweet_concept = {
        'id': tweet.get('id', None),
        'text': tweet.get('text', None),
        'created_at': tweet.get('created_at', None),
        'likes': tweet.get('likes', None),
        'retweets': tweet.get('retweets', None)
    }

    words = word_tokenize(tweet_concept['text'])
    likes = tweet_concept['likes']
    retweets = tweet_concept['retweets']
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.lower() not in custom_stopwords and word.isalnum()]
    pos_tags = pos_tag(filtered_words)
    nouns = [word for word, pos in pos_tags if pos.startswith('N')]
    all_nouns.extend(nouns)
    for w in  nouns:
        if w in word_like:
            word_like[w] += int(likes)
            word_retweet[w] += int(retweets)
        else:
            word_retweet[w] = int(retweets)
            word_like[w] = int(likes)

noun_pop = {}
freq_dist = FreqDist(all_nouns)
top_nouns = freq_dist.most_common()
for w, frequency in top_nouns:
    norm_retweet = (word_retweet.get(w, 0) - min(word_retweet.values())) / (max(word_retweet.values()) - min(word_retweet.values()))
    norm_likes = (word_like.get(w, 0) - min(word_like.values())) / (max(word_like.values()) - min(word_like.values()))

    popularity = frequency * (1.4 + norm_retweet) * (1.2 + norm_likes)
    noun_pop[w] = popularity

sorted_noun_pop = dict(sorted(noun_pop.items(), key=lambda item: item[1], reverse=True))

for i, (noun, score) in enumerate(sorted_noun_pop.items()):
    print(f"{noun}: {score}")
    if i == 9:
        break
