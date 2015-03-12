# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:18:31 2015

@author: Jeremy
"""
import csv

def splitTestTrainingData(file, trainingPercentage):
    postData = []
    with open(file, 'r') as csvfile:
        postReader = csv.reader(csvfile, delimiter=',')
        evens = 0;
        for row in postReader:
            if(evens%2 == 0):
                postData.append(row)
            evens += 1
    cutoff = int(len(postData)*trainingPercentage)
    return postData[1:cutoff], postData[cutoff:]
    
def formatForBernoulli(file, trainingPercentage):
    trainingData, testData = splitTestTrainingData(file, trainingPercentage)
    formatTrainingData = []
    formatTestData = []
    frontPageSuccess = []
    for i in trainingData:
        formatTrainingData.append(i[1:-2])
        frontPageSuccess.append(i[-2])
    for i in testData:
        formatTestData.append(i[1:-2])
        
    return formatTrainingData, formatTestData, frontPageSuccess
    
    
        
    
if __name__ == "__main__":
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\sample.csv"
    trainingData, testData, frontPage = formatForBernoulli(fileName, .25)
    print("Size of training data is: " + str(len(trainingData)))    
    print(trainingData[0])
    print()
    print("Size of test data is: " + str(len(testData)))
    print(testData[0])
    
            