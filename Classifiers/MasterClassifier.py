# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:54:06 2015

@author: Jeremy
"""

from sklearn.metrics import mean_squared_error

from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier

import splitTestTrainingData

#################################################################################################################################################
#################################################################################################################################################

# INITIALIZING CLASSIFIERS
# Each classifier takes training data and a vector representing the class information, initializes the classifier, and fits the data
def createAdaBoostClassifier(trainingVectors, targetValues):
    

    clf = AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
    clf.fit(trainingVectors, targetValues, targetValues*10000)
    
    return(clf)
    
    
def RandForestClassifier(trainingVectors, targetValues):
    
    clf = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None, min_samples_split=1, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, min_density=None, compute_importances=None)
    clf.fit(trainingVectors, targetValues, targetValues*10000)
    
    return(clf)
    
    
def createSGDClassifier(trainingVectors, targetValues):
    
    clf  = SGDClassifier(loss='hinge', penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, n_iter=5, shuffle=False, verbose=0, epsilon=0.1, n_jobs=1, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, class_weight=None, warm_start=False)    
    clf.fit(trainingVectors, targetValues)
    
    return(clf)

    
def bernNBClassifier(trainingVectors, targetValues):
    
    clf = BernoulliNB()    
    clf.fit(trainingVectors, targetValues, targetValues*10000)
    
    return(clf)

##############################################################################################################################################
##############################################################################################################################################

#output function to output the accuracy percentage, and the predictions for the test data
def outputPredictions(predictions, accuracy):
    #ToDo get program to output to separate files
    outfile = open("C:\\Users\\Jeremy\\Documents\\CS 175\\predictionsBernoulli.csv", 'w')
    outfile.write(str(accuracy) + "\n")
    for i in predictions:
        outfile.write(str(i) + "\n")
    outfile.close()

#Takes a file path as a string, runs Bernoulli Naive Bayes classifier on the data.
def runClassifier(filename):
    trainingData, testData, frontPage, testFrontPage = splitTestTrainingData.formatForBernoulli(fileName, .75)
    
    clf1 = createAdaBoostClassifier(trainingData, frontPage)
    clf2 = RandForestClassifier(trainingData, frontPage)
    clf3 = createSGDClassifier(trainingData, frontPage)
    clf4 = bernNBClassifier(trainingData, frontPage)

    predictions = []
    predictions.append(clf1.predict(testData))
    predictions.append(clf2.predict(testData))
    predictions.append(clf3.predict(testData))
    predictions.append(clf4.predict(testData))
    
    print("MSE: ")
    print(mean_squared_error(testFrontPage, predictions[0]))
    
    #values to track the accumulated 'total' points and the 'correct' points, represented
    #    represented by the given weights

    
    #weights for correctly/incorrectly guessing a post will/won't make it to the front page
    frontPageWeight = 100
    notFrontPageWeight = 1
    
    percentages = []
    #calculates accuracy with given weights
    for j in predictions:
        correct = 0
        total = 0
    
        fcorrect = 0
        ftotal = 0
        for i in range(len(j)):
            if(testFrontPage[i] == 1):
                total += frontPageWeight
                ftotal += 1
                if(j[i] == testFrontPage[i]):
                    fcorrect += 1
                
            else:
                total += notFrontPageWeight
            if((j[i] == testFrontPage[i]) and (j[i] == 1)):
                correct += frontPageWeight
            elif((j[i] == testFrontPage[i]) and (j[i] == 0)):
                correct += notFrontPageWeight
        percentages.append(correct/total)
            
    #returns the accuracy as a percentage    
#    print("How many times predicter accurately predicted a post making the front page: ")
#    print(fcorrect/ftotal)
#    print("Correct guesses: " + str(fcorrect))
#    print("Total front page posts: " + str(ftotal))
    for j in predictions:
        outputPredictions(j, (correct/total)) 

    
    
if __name__ == "__main__":
        
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\NEWdataBETTERdataUSEthis.csv"
    runClassifier(fileName)
