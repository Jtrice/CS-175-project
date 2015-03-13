# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:54:06 2015

@author: Jeremy
"""

from sklearn.naive_bayes import BernoulliNB
#from sklearn.ensemble import AdaBoostClassifier
#from sklearn.linear_model import SGDClassifier
#from sklearn.ensemble import RandomForestClassifier
#import numpy as np
import splitTestTrainingData


#Takes the training data as a list of lists, the classes for each list, and the values to be predicted,
#   and returns the predictions.
def bernNBClassifier(trainingVectors, targetValues, valueForPrediction):
    
    clf = BernoulliNB()
    #clf = AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
    #clf  = SGDClassifier(loss='hinge', penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, n_iter=5, shuffle=False, verbose=0, epsilon=0.1, n_jobs=1, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, class_weight=None, warm_start=False)
    #clf = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None, min_samples_split=1, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, min_density=None, compute_importances=None)
    clf.fit(trainingVectors, targetValues)
    
    #taken from the example, likely needs to change with predictions. 
    return(clf.predict(valueForPrediction))


#output function to output the accuracy percentage, and the predictions for the test data
def outputPredictions(predictions, accuracy):
    outfile = open("C:\\Users\\Jeremy\\Documents\\CS 175\\predictions.csv", 'w')
    outfile.write(str(accuracy) + "\n")
    for i in predictions:
        outfile.write(i + "\n")
    outfile.close()

#Takes a file path as a string, runs Bernoulli Naive Bayes classifier on the data.
def runBernoulliNBClassifier(filename):
    trainingData, testData, frontPage, testFrontPage = splitTestTrainingData.formatForBernoulli(fileName, .75)
    predictions = bernNBClassifier(trainingData, frontPage, testData)
    
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
        if(testFrontPage[i] == '1'):
            total += frontPageWeight
            ftotal += 1
            if(predictions[i] == testFrontPage[i]):
                fcorrect += 1
            
        else:
            total += notFrontPageWeight
        if((predictions[i] == testFrontPage[i]) and (predictions[i] == '1')):
            correct += frontPageWeight
        elif((predictions[i] == testFrontPage[i]) and (predictions[i] == '0')):
            correct += notFrontPageWeight
            
    #returns the accuracy as a percentage    
    print("How many times predicter accurately predicted a post making the front page: ")
    print(fcorrect/ftotal)
    print("Correct guesses: " + str(fcorrect))
    print("Total front page posts: " + str(ftotal))
    outputPredictions(predictions, (correct/total))    
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