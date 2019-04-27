#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
def seg_word(sentence):
    seg_list = jieba.cut(sentence)
    seg_result = []
    for w in seg_list:
        seg_result.append(w)
    return seg_result

doc1 = '空气质量良轻度污染空气质量指数125首要污染物为细颗粒物'
doc2 = '美国环境保护署估计空气在室内污染的严重程度可能比室外污染高8倍'
doc3 = '天然矿泉水是指从地下深处自然涌出的或钻井采集的含有一定量的矿物质微量元素或其他成分'
seg1 = seg_word(doc1)
seg2 = seg_word(doc2)
seg3 = seg_word(doc3)
corpus = []
corpus.append(' '.join(seg1))
corpus.append(' '.join(seg2))
corpus.append(' '.join(seg3))
tfidf_vectorizer = TfidfVectorizer()
tfidf_count = tfidf_vectorizer.fit_transform(corpus).todense()
print(tfidf_vectorizer.vocabulary_)
print(tfidf_vectorizer.fit_transform(corpus).todense())
for x, y in [[0, 1], [0, 2]]:
    print('sssss', tfidf_count[x])
    dist = euclidean_distances(tfidf_count[x], tfidf_count[y])
    print('文档{}与文档{}的距离{}'.format(x, y, dist))
'''
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
aa = [1,2,3,4,5]
bb = [1,3,4,4,2]
dist = euclidean_distances(np.array([aa]), np.array([bb]))
print(dist)