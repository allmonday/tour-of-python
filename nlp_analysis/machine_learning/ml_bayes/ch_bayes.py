
#coding=utf-8
from __future__ import division
from numpy import *
import jieba
from collections import Counter

#bayes classifier: to tell the price is cheap of expensive
CHEAP_TRAINNING = './training/cheap_train.txt'
EXPENSIVE_TRAINNING = './training/expensive_train.txt'
STOP_WORDS = set(['。', '，', ',', '.','“','”','、','\n',' ','　','（',
'）','【','】', '...', '>', '<', '!', '！', '我','的','是' ,'也'])

def cut_with_stop_words(sentenct):
    return_value = []
    raw_cut = jieba.cut(sentenct, cut_all = False)
    for each in raw_cut:
        if each in STOP_WORDS:
            continue
        else:
            return_value.append(each)
    return return_value

def loadDataSet():
    #1.load cheap
    cheap_dataset = [cut_with_stop_words(line) for line in open(CHEAP_TRAINNING, 'r').readlines()]
    classVec = [0] * len(cheap_dataset) #0 is cheap
    #2.load expensive
    expensive_dataset = [cut_with_stop_words(line) for line in open(EXPENSIVE_TRAINNING, 'r').readlines()]
    classVec.extend([1]* len(expensive_dataset)) #1 is expensive
    postingList = cheap_dataset + expensive_dataset
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet) 

def bagOfWords2Vec(vocabList, inputSet):
    ''' space for whole vector'''
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    #    else:
    #        print "the word: %s is not in my Vocabulary!"% word
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/ numTrainDocs   #length of category
    p0Num = ones(numWords); p1Num = ones(numWords)  # np.arry([0,0,0,0])
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs): #for now , 6 lines
        if trainCategory[i] == 1: #craps here!!!
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i]) #count all '1's
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom) #sum of all contributes will be 1
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect,pAbusive # 子概率，　先验概率

def classifyNB(vec2Classify,p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1) # posibility of good 
    #print('p0, cheap',p0)
    #print('p1, expensive',p1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNb():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    #print(myVocabList)
    #print(len(myVocabList))
    #print(type(myVocabList))
    #exit()

    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(bagOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)  

    #test the expensive group
    count = 0
    total = 0
    for line in open('./test/expensive_test.txt','r').readlines():
        testEntry = cut_with_stop_words(line) 
        thisDoc = array(bagOfWords2Vec(myVocabList, testEntry))
        ret = classifyNB(thisDoc, p0V, p1V, pAb)
        total +=1
        count += (1-ret)
        #print( testEntry, 'classified as:', ret)
        #input()
    print('expensive',count, total)

    count = 0
    total = 0
    #test the cheap group
    for line in open('./test/cheap_test.txt','r').readlines():
        testEntry = cut_with_stop_words(line) 
        thisDoc = array(bagOfWords2Vec(myVocabList, testEntry))
        ret = classifyNB(thisDoc, p0V, p1V, pAb)
        total +=1
        count += ret
        #print( testEntry, 'classified as:', ret)
        #input()
    print('cheap',count, total)

if __name__ == "__main__":
    testingNb()
