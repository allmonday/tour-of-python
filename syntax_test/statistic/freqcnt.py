

class FreqCnt(object):


    def __init__(self, source, dictionary, output = 'output.txt'):
        self.text = open(source, 'r').read()
        self.dictionary = open(dictionary,'r').readlines()
        self.output = output

    def run(self):
        out = open(self.output, 'w')
        for w in self.dictionary:
            w1 = w.split(' ')[0]
            cnt = self.text.count(w1)
            if cnt > 0:
                print(w, cnt)
                out.write('%s\t%s\n'%(w1, cnt))
        out.close()

    def __call__(self):
        self.run()

if __name__ == "__main__":

    fc = FreqCnt('amazon_reviews.txt', 'dict.txt')
    fc()
