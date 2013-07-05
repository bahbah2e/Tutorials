from numpy import *
from math import log
import matplotlib
import matplotlib.pyplot as plt
import operator

def classify0(inX, dataSet, labels, k):
    distances = distanceCalculation(inX, dataSet)
    sortedDistIndicies = distances.argsort()    
    classCount=classes(labels,sortedDistIndicies,k)    
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def plotfilematrix(filename):
    dataset,labels = file2matrix(filename)
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataset[:,1], dataset[:,2])
    return plt.show()

def createTreeDataSet():
    dataset = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels=['no surfacing', 'flippers']
    return dataset, labels

def calcShannonEnt(dataset):
    shannonEnt = 0.0
    numEntries = len(dataset)
    labelCounts=getLabelCounts(dataset)

    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt -= prob *log(prob,2)
    return shannonEnt

def getLabelCounts(dataset):
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            print('Is fish? %s' % ( currentLabel))
        labelCounts[currentLabel] += 1
    return labelCounts

    