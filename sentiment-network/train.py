import numpy as np
import pandas as pd
from collections import Counter

with open('reviews.txt') as f:
    reviews = list(map(lambda x: x[:-1], f.readlines()))

with open('labels.txt') as f:
    labels = list(map(lambda x: x[:-1], f.readlines()))

positive_counter = Counter()
negative_counter = Counter()

assert len(reviews) == len(labels)

for i in range(len(reviews)):
    sentence = reviews[i].replace('.', '').split()
    if labels[i] == 'positive':
        for word in sentence:
            positive_counter[word] += 1
    else:
        for word in sentence:
            negative_counter[word] += 1

#positive_counter = list(filter(lambda x: x[1] > 100, positive_counter.items()))

pos_neg_ratios = Counter()

for word in positive_counter:
    if positive_counter[word] >= 100:
        pos_neg_ratios[word] = np.log(positive_counter[word] / float(negative_counter[word] + 1))

print(pos_neg_ratios['the'])
print(pos_neg_ratios['amazing'])
print(pos_neg_ratios['terrible'])
