# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:54:06 2015

@author: Jeremy
"""

from sklearn.naive_bayes import BernoulliNB
#import numpy as np
import splitTestTrainingData


#Takes the training data as a list of lists, the classes for each list, and the values to be predicted,
#   and returns the predictions.
def bernNBClassifier(trainingVectors, targetValues, valueForPrediction):
    
    clf = BernoulliNB()
    clf.fit(trainingVectors, targetValues)
    
    #taken from the example, likely needs to change with predictions. 
    return(clf.predict(valueForPrediction))


#Takes a file path as a string, runs Bernoulli Naive Bayes classifier on the data.
def runBernoulliNBClassifier(filename):
    trainingData, testData, frontPage, testFrontPage = splitTestTrainingData.formatForBernoulli(fileName, .25)
    predictions = bernNBClassifier(trainingData, frontPage, testData)
    
    #values to track the accumulated 'total' points and the 'correct' points, represented
    #    represented by the given weights
    correct = 0
    total = 0
    
    #weights for correctly/incorrectly guessing a post will/won't make it to the front page
    frontPageWeight = 100
    notFrontPageWeight = 1
    
    #calculates accuracy with given weights
    for i in range(len(predictions)):
        if(testFrontPage[i] == '1'):
            total += frontPageWeight
        else:
            total += notFrontPageWeight
        if((predictions[i] == testFrontPage[i]) and (predictions[i] == '1')):
            correct += frontPageWeight
        elif((predictions[i] == testFrontPage[i]) and (predictions[i] == '0')):
            correct += notFrontPageWeight
            
    #returns the accuracy as a percentage        
    return(correct/total)
    
    
if __name__ == "__main__":
    
    #Test values for the bernoulli classifer, not used when run. 
    #x = np.random.randint(2, size=(6,100))
    #y = np.array([1,2,3,4,4,5])
    
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\NEWdataBETTERdataUSEthis.csv"
    print(runBernoulliNBClassifier(fileName))

    #gets the predictions from the classifier    
    #print(bernNBClassifier(x, y, x[2]))
    
    
    #tracks how many correct answers the predictions get, needs weights added
    

    
    
    #print(trainingData)
    #print(len(testData[0]))
    #print(len(trainingData))