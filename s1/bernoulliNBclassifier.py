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
    #x = np.random.randint(2, size=(6,100))
    #y = np.array([1,2,3,4,4,5])
    
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\sample - Copy.csv"
    trainingData, testData, frontPage, testFrontPage = splitTestTrainingData.formatForBernoulli(fileName, .25)


    #gets the predictions from the classifier    
    #print(bernNBClassifier(x, y, x[2]))
    predictions = bernNBClassifier(trainingData, frontPage, testData)
    
    #tracks how many correct answers the predictions get, needs weights added
    correct = 0
    for i in range(len(predictions)):
        if(predictions[i] == testFrontPage[i]):
            correct += 1
    print(correct/(len(predictions)))
    
    
    #print(trainingData)
    #print(len(testData[0]))
    #print(len(trainingData))