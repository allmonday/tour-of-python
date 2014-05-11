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
'）','【','】', '...', '>', '<', '!', '！','?',
'了','的','很','还','买','是','不','吧', '有','就','我','在','？','这','一个']) 



class CompareMan(object):
    def __init__(self,arg, sfile):
        if arg== '-t':
            self.text = sfile
        else:
            self.text = open(sfile, 'r').readlines()
        #self.dictionary = dictionary
    def process(self):
        self.wordSet = Counter()
        for line in self.text:
            cutted = jieba.cut(line, cut_all=False)
            return_line = []
            for w in cutted:
                if w in stop_words:
                    continue
                else:
                    self.wordSet[w] += 1
        return self.wordSet


    def __call__(self):
        self.process()
        rec = self.wordSet.most_common()
        for i,j in rec:
            print(i,' ',j)


if __name__ == "__main__":
    c = CompareMan('aa', 'beer_jd_unique.txt')
    c()
