#coding=utf-8
'''
desciption:
    calc the freq of each word in target file
    - some character should be removed first..
'''

stop_words= set([
    "the","of","is","and","to","in","that","we","for","an","are","by","be","as",
    "on","with","can","if","from","which","you","it","this","then","at","have",
    "all","not","one","has","or","that" ])

lines = open('voa.txt').readlines()

freq = {}
for line in lines:
    for w in line.split(' '):
        if w.strip().lower() in stop_words: continue  #skip popular word
        freq[w] = freq.get(w, 0) + 1  #use get() method to initialize value

sfreq = sorted(freq.items(), key=lambda e: e[1], reverse=True)

for f, c in sfreq:
    print c, '--', f

