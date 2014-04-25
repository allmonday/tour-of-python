import re

class Stat(object):
    def __init__(self, text, keyword1, keyword2):
        self.text = text
        self.keyword1 = keyword1
        self.keyword = keyword1 + keyword2
        
    def __call__(self):
        p1 = self.text.count(self.keyword1)
        p2 = self.text.count(self.keyword)
        #print(p1)
        #print(p2)
        print("%s: p(wi) -> %d"%(self.keyword1, p1))
        print("%s: p(wi-1, wi) -> %d"%(self.keyword, p2))
        print('p(wi/ wi-1) = %f%%'%(100 * (p2/ p1)))


if __name__ == "__main__":
    sampleText = open('../amazon_reviews.txt','r').read()
    test_table = [["口感", "不错"],
                  ["质", "量"],
                  ["价", "格"],
                  ["很", "不错"],
                  ["还", "不错"]
            ]
    for g in test_table:
        stat = Stat(sampleText, g[0], g[1])
        stat()
        print()
