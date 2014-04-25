#coding=utf-8
import yaml
import re

def load_yaml(fp):
    try:
        return yaml.load(open(fp, encoding='utf-8'))
    except (TypeError, FileNotFoundError, ParserError):
        return {}

posi_word = load_yaml('positive_adj.yml')
nega_word = load_yaml('negative_adj.yml')
turning_word = ['但是', '可是', '不过', '没想到', '发现', '结果', '竟然',
'居然', '还好', '好在']

class TurningFinder(object):
    def __init__(self, file, bk=False):
        self.file = file
        self.bk = bk
        self.count = 0

    def _word_in_sentence(self ,words, sentence):
        for w in words:
            if w in sentence:
                return  w
        return False
        
    def run(self):
        with open(self.file, 'r') as f:
            for line in f.readlines():
                ret = self._word_in_sentence(turning_word, line)
                if ret:
                    print('>>>',line),
                    print(ret,'\n', '\n'.join(line.strip().split(ret))),
                    if self.bk:
                        input()
                    self.count += 1
            print(self.count)

if __name__ == "__main__":

        t = TurningFinder('amazon_reviews.txt', bk=True)
        #t = TurningFinder('amazon_reviews.txt', bk=False)
        t.run()
