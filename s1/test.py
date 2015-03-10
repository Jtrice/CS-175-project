import numpy as np
from sklearn import tree
import time

X1 = np.loadtxt(fname = "kaggle.X1.train.txt", delimiter = ',')
Y = np.loadtxt(fname = "kaggle.Y.train.txt", delimiter = ',')
print("Loaded Data")

t = time.time()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X1, Y)
print("Build Learner in {} seconds".format( (time.time()-t)/60) )

Xtest = np.loadtxt(fname = "kaggle.X1.test.txt", delimiter = ',')
Yhat = clf.predict(Xtest)
print("Prediction {} made".format(Yhat))
