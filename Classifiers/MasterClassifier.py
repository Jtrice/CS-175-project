# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:54:06 2015

@author: Jeremy
"""

#from sklearn.metrics import mean_squared_error
import numpy as np

from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier

import splitTestTrainingData

#################################################################################################################################################
#################################################################################################################################################

# INITIALIZING CLASSIFIERS
# Each classifier takes training data and a vector representing the class information, initializes the classifier, fits the data, and returns the classifier
def createAdaBoostClassifier(trainingVectors, targetValues, weights):
    

    clf = AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
    clf.fit(trainingVectors, targetValues, weights)
    
    return(clf)
    
    
def RandForestClassifier(trainingVectors, targetValues, weights):
    
    clf = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None, min_samples_split=1, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, min_density=None, compute_importances=None)
    clf.fit(trainingVectors, targetValues, weights)
    
    return(clf)
    
    
def createSGDClassifier(trainingVectors, targetValues):
    
    clf  = SGDClassifier(loss='hinge', penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, n_iter=5, shuffle=False, verbose=0, epsilon=0.1, n_jobs=1, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, class_weight=None, warm_start=False)    
    clf.fit(trainingVectors, targetValues)
    
    return(clf)

    
def bernNBClassifier(trainingVectors, targetValues, weights):
    
    clf = BernoulliNB()    
    clf.fit(trainingVectors, targetValues, weights)
    
    return(clf)

##############################################################################################################################################
##############################################################################################################################################

#output function to output the accuracy percentages and predictions for the test data
def outputPredictions(predictions, accuracy):
    outfile = open("C:\\Users\\Jeremy\\Documents\\CS 175\\predictionsALLJeremy.csv", 'w')
    outString = ""
    
    # Output accuracy of each classifier at top of column
    for i in accuracy:
        outString += str(i) + ","
    outfile.write(outString + "\n")
    
    # Output prediction of each classifier in appropriate column/row
    for i in range(len(predictions[0])):
        outString = ""
        for j in predictions:
            outString += str(j[i]) + ","
        outfile.write(outString + "\n")
    
    outfile.close()

###############################################################################################################################################
###############################################################################################################################################

def accuracyOfPredictions(predictions, frontPage):
    #weights for correctly/incorrectly guessing a post will/won't make it to the front page
    frontPageWeight = 100
    notFrontPageWeight = 1
    
    percentages = []
    #calculates accuracy with given weights, needs to be adjusted
    for j in predictions:
        #ToDo: calculates mean squared error for one classifier, either needs to be used on all or removed
        #print("MSE: ")
        #percentages.append(1-(mean_squared_error(frontPage, j)))
        correct = 0
        total = 0
    
        fcorrect = 0
        fincorrect = 0
        ftotal = 0
        for i in range(len(j)):
            if(frontPage[i] == 1):
                total += frontPageWeight
                ftotal += 1
                if(j[i] == frontPage[i]):
                    fcorrect += 1
                
            else:
                total += notFrontPageWeight
            if(j[i] == 1 and frontPage[i] == 0):
                fincorrect += 1
            if((j[i] == frontPage[i]) and (j[i] == 1)):
                correct += frontPageWeight
            elif((j[i] == frontPage[i]) and (j[i] == 0)):
                correct += notFrontPageWeight
        percentages.append(fcorrect/ftotal)
    return percentages



###############################################################################################################################################
###############################################################################################################################################
#Takes a file path as a string, runs all classifiers on the data, and outputs all predictions and accuracy rating to .csv file.
def runClassifier(filename):
    # calls function to read in data, truncate non-boolean values and return data for training and testing.
    trainingData, testData, frontPage, testFrontPage = splitTestTrainingData.formatForBernoulli(fileName, .75)
    
    # Initialize a list holding weights for each post based on if it made the front page
    frontPageWeighting = 10
    weights = []
    
    for i in range(len(frontPage)):
        weights.append((frontPage[i]*frontPageWeighting) + 1)
    
    weights = np.array(weights)    
        
    # Initializing all classifiers and fiting training data.
    clf1 = createAdaBoostClassifier(trainingData, frontPage, weights)
    clf2 = RandForestClassifier(trainingData, frontPage, weights)
    clf3 = createSGDClassifier(trainingData, frontPage)
    clf4 = bernNBClassifier(trainingData, frontPage, weights)

    # Get all predictions from test data
    predictions = []
    predictions.append(clf1.predict(testData))
    predictions.append(clf2.predict(testData))
    predictions.append(clf3.predict(testData))
    predictions.append(clf4.predict(testData))
    
    # Combines all data into one list, and runs predictions on it.
    predictionsALL = []
    allData = []
    allData.extend(trainingData)
    allData.extend(testData)
    
    predictionsALL.append(clf1.predict(allData))
    predictionsALL.append(clf2.predict(allData))
    predictionsALL.append(clf3.predict(allData))
    predictionsALL.append(clf4.predict(allData))
    
    # Sends predictions and accuracy of classifiers to output function
    outputPredictions(predictionsALL, accuracyOfPredictions(predictions, testFrontPage)) 

##################################################################################################################################################
##################################################################################################################################################
    
if __name__ == "__main__":
        
    fileName = "C:\\Users\\Jeremy\\Documents\\CS 175\\NEWdataBETTERdataUSEthis.csv"
    runClassifier(fileName)
