# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:54:06 2015

@author: Jeremy
"""

from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
import splitTestTrainingData


#Takes the training data as a list of lists, the classes for each list, and the values to be predicted,
#   and returns the predictions.
def RandForestClassifier(trainingVectors, targetValues):
    
    clf = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None, min_samples_split=1, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, min_density=None, compute_importances=None)
    clf.fit(trainingVectors, targetValues, targetValues*10000)
    
    return(clf)


#output function to output the accuracy percentage, and the predictions for the test data
def outputPredictions(predictions, accuracy):
    outfile = open("C:\\Users\\Jeremy\\Documents\\CS 175\\predictionsRandomForest.csv", 'w')
    outfile.write(str(accuracy) + "\n")
    for i in predictions:
        outfile.write(str(i) + "\n")
    outfile.close()

#Takes a file path as a string, runs Bernoulli Naive Bayes classifier on the data.
def runRandForestClassifier(filename):
    trainingData, testData, frontPage, testFrontPage = splitTestTrainingData.formatForBernoulli(fileName, .75)
    clf = RandForestClassifier(trainingData, frontPage)
    predictions = clf.predict(testData)
    
    print("MSE: ")
    print(mean_squared_error(testFrontPage, predictions))
    
    #values to track the accumulated 'total' points and the 'correct' points, represented
    #    represented by the given weights
    correct = 0
    total = 0
    
    fcorrect = 0
    ftotal = 0
    
    #weights for correctly/incorrectly guessing a post will/won't make it to the front page
    frontPageWeight = 100
    notFrontPageWeight = 1
    
    #calculates accuracy with given weights
    for i in range(len(predictions)):
        if(testFrontPage[i] == 1):
            total += frontPageWeight
            ftotal += 1
            if(predictions[i] == testFrontPage[i]):
                fcorrect += 1
            
        else:
            total += notFrontPageWeight
        if((predictions[i] == testFrontPage[i]) and (predictions[i] == 1)):
            correct += frontPageWeight
        elif((predictions[i] == testFrontPage[i]) and (predictions[i] == 0)):
            correct += notFrontPageWeight
            
    #returns the accuracy as a percentage    
#    print("How many times predicter accurately predicted a post making the front page: ")
#    print(fcorrect/ftotal)
#    print("Correct guesses: " + str(fcorrect))
#    print("Total front page posts: " + str(ftotal))
    outputPredictions(predictions, (correct/total)) 
    return(correct/total)
    
    
if __name__ == "__main__":
        
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\NEWdataBETTERdataUSEthis.csv"
    print(runRandForestClassifier(fileName))
