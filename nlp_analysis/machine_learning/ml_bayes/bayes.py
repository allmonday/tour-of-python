#coding=utf-8
from __future__ import division
from numpy import *

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'fiea', 'problems','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1]
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
    if p1 > p0:
        return 1
    else:
        return 0

def testingNb():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(bagOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)  
    testEntry = ['love', 'my' ,'damation']
    thisDoc = array(bagOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb)

    testEntry = ['stupid', 'dog']
    thisDoc = array(bagOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb)


if __name__ == "__main__":
    testingNb()
