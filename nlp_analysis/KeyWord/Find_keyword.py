#coding=utf-8

'''
    use if-idf algorithm to find key words in articles
    also can be used in short sentence however the proformance is not so good.
'''
import sys
import jieba
from collections import Counter
jieba.user_dict = "./dictionary/user_dict.txt"
stop_words = set(['。', '，', ',', '.','“','”','、','\n',' ','　','（',
'）','【','】', '...', '>', '<', '!', '！']) 
idf_content = open('./dictionary/idf.txt','rb').read().decode('utf-8').split('\n')
idf_freq = {}
for line in idf_content:
    word, freq = line.split(' ')
    idf_freq[word]= float(freq)


class CompareMan(object):
    def __init__(self,arg, sfile):
        if arg== '-t':
            self.text = sfile
        else:
            self.text = open(sfile, 'r').read()
        #self.dictionary = dictionary

    def _get_cutted(self):
        cnt = Counter()
        self._cutted_content = (jieba.cut(self.text, cut_all = False))
        for word in self._cutted_content:
            if word not in stop_words:
                cnt[word] += 1
        self.total = sum(cnt.values())
        return cnt

    def _calc_weight(self):
        self.common =dict(self._get_cutted().most_common(20))
        for k in self.common:
            self.common[k] *= (idf_freq.get(k, 10)/self.total)
        return sorted(self.common.items(), key=lambda x:x[1], reverse=True)

    def __call__(self):
        self._get_cutted()
        return self._calc_weight()[:10]

if __name__ == "__main__":
    for line in open('./data/amazon_reviews.txt','r').readlines():
        print(line)
        c = CompareMan('-t', line)
        print(c())
        input()
