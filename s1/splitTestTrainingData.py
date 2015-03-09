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
    
if __name__ == "__main__":
    fileName = "E:\\sample.csv"
    trainingData, testData = splitTestTrainingData(fileName, .25)
    print("Size of training data is: " + str(len(trainingData)))    
    print(trainingData[0])
    print()
    print("Size of test data is: " + str(len(testData)))
    print(testData[0])
    
            