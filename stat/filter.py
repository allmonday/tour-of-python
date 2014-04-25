from collections import Counter

def get_feature_word(text, basic_dict = "basic_dictionary.txt"):

    '''feature =  word appear mostly - high weight word
       based on: IF-IDF 
    '''
    list_a = open(basic_dict,'r').readlines()
    list_b = open('next.txt','r').readlines()
    symmetric_diff = set(list_a) ^ set(list_b)
    diff = set(list_b) - set(list_a) 

    print(symmetric_diff)
    print(diff)

def get_Freq_count(text):
    cnt = Counter(text.split(' ')) 
    return cnt
