import nltk
import sys


pos_list = set()
with open("positive-words.txt") as pw:
    for line in pw.readlines():
        if line.startswith(';'):
            continue
        pos_list.add(line.rstrip())  # After removing new line char
neg_list = set()
with open("negative-words.txt") as ng:
    for line in ng.readlines():
        if line.startswith(';'):
            continue
        neg_list.add(line.rstrip())  # After removing new line char
with open("raven.txt") as txt:
    text = txt.read()

    #for text in text.split():
    pos_count = 0
    neg_count = 0
    tot_count = 0

    for word in text.split():
        print text.split()[:10]
        if word in pos_list:
            pos_count += 1
        if word in neg_list:
            neg_count += 1
        tot_count + 1
        if tot_count == 0:
            continue
    subjectivity = 1.0 * (pos_count + neg_count) / tot_count
    polarity = 1.0 * (pos_count - neg_count) / tot_count
    print pos_count
    print subjectivity
    print polarity
