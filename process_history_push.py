#coding:utf-8
import jieba
import glob

history = {}
def stopWords_():
    stops = []
    with open('stops.txt', encoding='utf-8') as fr:
        for line in fr:
            stops.append(line.strip())
    return stops
stopWords = stopWords_()

def getCuts(pathfilename, cutfile):
    fw = open(cutfile, 'w')
    filenames = glob.glob(pathfilename)
    for filename in filenames:
        tmp = []
        with open(filename, encoding='utf-8') as fr:
            for line in fr:
                if line.strip():
                    tmp.append(line.strip())
        # print(filename.split('\\')[-1].split('.')[0], ' '.join(tmp))
        try:
            fw.write(filename.split('\\')[-1].split('.')[0]+'\t'+' '.join([x for x in jieba.cut(' '.join(tmp)) if x not in stopWords]) + '\n')
        except:
            pass
        # history[filename.split('\\')[-1].split('.')[0]] = ' '.join(tmp)

getCuts('../NewsPushDir/*', 'push_cut.txt')