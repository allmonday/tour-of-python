from collections import Counter

cnt = Counter()
for word in open('output100.txt').readlines():
    w, c = word.split('\t')
    cnt[w] = int(c.strip())

print(cnt.most_common(100))

    

