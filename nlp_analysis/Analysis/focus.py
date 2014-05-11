import yaml
#1.import file
#2.set key word
#3.if find keyword, print line
keywords = yaml.load(open('focus.yaml'))

def key_filter(sentence):
    for k in keywords:
        if k in sentence and not any(kf in sentence for kf in keywords[k]):
            return True
    return False

lines = open('./data/amazon_reviews.txt', 'r').readlines()
for line in lines:
    if key_filter(line):
        print(line)
        input()
    else:
        continue
