# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:52:21 2017

@author: caenglish
"""
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from collections import Counter

#From https://www.youtube.com/watch?v=W4kqEvGI4Lg
class do_ML:
    
    def do_ml(X, y, df):
        #What about http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html to preserve time ordering?
        X_train, X_test, y_train, y_test=cross_validation.train_test_split(X, y, test_size=0.25)
        
        #clf_KN=neighbors.KNeighborsClassifier()
        
        clf=VotingClassifier([('lsvc',svm.LinearSVC()),
                              ('knn',neighbors.KNeighborsClassifier()),
                              ('rfor', RandomForestClassifier())])
        
        clf.fit(X_train,y_train)
        confidence = clf.score(X_test, y_test)
        predictions = clf.predict(X_test)
        print('Predicted spread:', Counter(predictions))
        print('Accuracy:', confidence)
        
        return confidence