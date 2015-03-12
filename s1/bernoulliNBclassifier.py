# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:54:06 2015

@author: Jeremy
"""

from sklearn.naive_bayes import BernoulliNB
#import numpy as np
import splitTestTrainingData


def bernNBClassifier(trainingVectors, targetValues, valueForPrediction):
    
    clf = BernoulliNB()
    clf.fit(trainingVectors, targetValues)
    
    #taken from the example, likely needs to change with predictions. 
    return(clf.predict(valueForPrediction))
    
if __name__ == "__main__":
    
    #Test values for the bernoulli classifer, not used when run. 
    #X = np.random.randint(2, size=(6,100))
    #Y = np.array([1,2,3,4,4,5])
    
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\sample.csv"
    trainingData, testData, frontPage = splitTestTrainingData.formatForBernoulli(fileName, .25)
    
    #print(len(trainingData))
    #print(len(trainingData[0]))
    #print(len(frontPage))
    #print(len(testData[0]))
    #prints the prediction from the classifier
    print(bernNBClassifier(trainingData, frontPage, testData[0]))
