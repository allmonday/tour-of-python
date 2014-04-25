from __future__ import division
from math import log
import operator


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        labelCounts[currentLabel] = labelCounts.get(currentLabel, 0) + 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = labelCounts[key]/numEntries
        shannonEnt -= (prob * log(prob,2))
    return shannonEnt
        
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  #2 features
    baseEntropy = calcShannonEnt(dataSet)        #total entropy
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):                 #try each feature
        featList = [example[i] for example in dataSet]   #get items in feature 
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:                           #each item
            subDataSet = splitDataSet(dataSet, i, value)   
            prob = len(subDataSet)/ len(dataSet)
            newEntropy += prob * calcShannonEnt(subDataSet)  #get new entropy
        infoGain = baseEntropy - newEntropy     #why sub?????
        print infoGain
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classCount:
        classCount[vote] = classCount.get(vote, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
            key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,
            bestFeat,value), subLabels)
    return myTree

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


if __name__ == "__main__":
    myDat, labels = createDataSet()
    myTree = createTree(myDat, labels)
    print myTree
