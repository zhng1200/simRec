import glob
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


def getAllCuts():
    cuts = []
    for filename in glob.glob('*_cut.txt'):
        print(filename)
        with open(filename) as fr:
            for line in fr:
                cuts.append(line.strip().split('\t')[-1])
    return cuts


# print(cuts)
cuts = getAllCuts()
print(cuts)

# vectorizer = TfidfVectorizer(ngram_range=(1, 1))
# tfidf = vectorizer.fit_transform(cuts)
# joblib.dump(vectorizer, 'tf_idf.m')

tfidf = joblib.load('tf_idf.m')
xx = ['国务院办公厅 近日 下发 推进 生育 职工基本 医疗保险 合并 实施 意见 意见 提到 生育 医疗 费用 纳入']
print(tfidf.transform(xx).toarray())
# print(dir(tfidf_))
print(tfidf.get_feature_names())
word = tfidf.get_feature_names()  # 获取词袋模型中的所有词语
weight = tfidf.transform(xx).toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
    for j in range(len(word)):
        if weight[i][j] == 0.0:
            continue
        else:
            print(word[j], weight[i][j])
