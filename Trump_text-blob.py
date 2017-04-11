import json
!pip install TextBlob
import string
import matplotlib.pyplot as plt
import re


def plot_text_blob(tweets):
    sub_list = []
    pol_list = []
    p = string.punctuation
    print p
    d = string.digits
    print d
    table_p = string.maketrans(p, len(p) * " ")
    table_d = string.maketrans(d, len(d) * " ")
    for tweet in tweets:
        s=tweet["text"].encode('utf-8')
        temp=re.sub(r'[^\x00-\x7F]+','', s)
        tb = TextBlob(temp)
        sub_list.append(tb.sentiment.subjectivity)
        pol_list.append(tb.sentiment.polarity)

    plt.hist(pol_list, bins=100)  # , normed=1, alpha=0.75)
    plt.xlabel('subjectivity score')
    plt.ylabel('sentence count')
    plt.grid(True)
    plt.savefig('subjectivity.pdf')
    plt.show()


if __name__ == '__main__':
    with open('tweet_stream_trump_10.json', 'r') as f:
        tweets = json.load(f)
    plot_text_blob(tweets)