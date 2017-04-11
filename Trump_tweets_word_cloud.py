import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
import nltk
import string
import re
import os


def steming_words(tweets):
    ps = PorterStemmer()
    tweet_text_lst=[]
    #tweet_text_words=[]
    stemed_words=[]
    p = string.punctuation
    d = string.digits
    table_p = string.maketrans(p, len(p) * " ")
    table_d = string.maketrans(d, len(d) * " ")
    for tweet in tweets:
        text=tweet["text"]
        temp=re.sub(r'[^\x00-\x7F]+','', text)
        temp_text=temp.encode('utf-8').translate(table_p)
        #print temp_text
        tweet_text_lst.append(temp_text.translate(table_d))
    tweet_txt=''.join(tweet_text_lst)
    #print tweet_txt
    #print tweet_text_lst
    for word in tweet_txt.split():
        #print word
        #print word
        stemed_words.append(ps.stem(word))
        #print stemed_words

    return stemed_words

def word_cloud(StopedWords):
    TextTweet=' '.join(StopedWords)
    #print TextTweet
    wordcloud = WordCloud().generate(TextTweet)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def stop_wrods(stemed_words):
    stopwords = nltk.corpus.stopwords.words('english')
    print stopwords
    StopedWords=[word.encode('utf-8') for word in stemed_words if word not in stopwords and len(word)>1]
    return StopedWords
    #print StopedWords


if __name__ == '__main__':

    with open('tweet_stream_trump_Florida.json', 'r') as f:
        tweets = json.load(f)
    stemed_words=steming_words(tweets)
    #print stemed_words
    StopedWords=stop_wrods(stemed_words)
    word_cloud(StopedWords)
