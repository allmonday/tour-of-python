count = 0
print(len('去'))
for line in open('amazon_reviews.txt','r').readlines():
    #l = len(line)
    #count[l] = count.get(l, 0) + 1
    if len(line) < 50:
        count += 1
print(count)
