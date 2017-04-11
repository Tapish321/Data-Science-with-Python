from wordcloud import WordCloud
import matplotlib.pyplot as plot
import nltk
stopwords = nltk.corpus.stopwords.words("English")
txt = open("raven.txt").read()
txt2 = ''
for word in txt.split():
	if len( word) == 1 or word in stopwords:
		continue
	txt2 += '{}'.format(word)
wordcloud = WordCloud(max_font_size = 35.0).generate(txt)
plot.figure()
plot.imshow(wordcloud)
plot.axis('off')
plot.show()