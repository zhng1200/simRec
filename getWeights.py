import glob
from sklearn.externals import joblib
tfidf = joblib.load('tf_idf.m')
xx = ['国务院办公厅 近日 下发 推进 生育 职工基本 医疗保险 合并 实施 意见 意见 提到 生育 医疗 费用 纳入']

history_feather = []
with open('history_cut.txt') as fr:
    for line in fr:
        history_feather.append(tfidf.transform([line.strip()]).toarray()[0])
# print(history_feather)
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
fw = open('id_contents_weighte.csv', 'w')
def getTargets(history_feather):
    targets = []
    with open('push_cut.txt') as fr:
        for line in fr:
            weigh = 0.0
            newline = line.strip().split('\t')
            y = tfidf.transform([newline[1]]).toarray()[0]
            for x in history_feather:
                dist = euclidean_distances([x], [y])[0][0]
                weigh+=dist
            fw.write(','.join([str(newline[0]), str(weigh / len(history_feather))]) + '\n')
getTargets(history_feather)

# print(tfidf.get_feature_names())
# word = tfidf.get_feature_names()  # 获取词袋模型中的所有词语
# weight = tfidf.transform(xx).toarray()