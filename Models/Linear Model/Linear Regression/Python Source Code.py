! pip install numpy

import numpy as np 

class LinearRegression():
    
    def __init__(self , fit_intercept = True , positve = False):
        
        self.coef_ = None
        self.intercept_ = None
        self.pre = []
        self.fit_intercept = fit_intercept
        self.positive = positive
        self.rank = np.linalg.matrix_rank(X_train)
        self.n_feautres_in = len(X_train.columns)
        self.feature_names_in_ = X_train.columns

    def fit(self , X_train , Y_train):

        num = 0
        den = 0
    
        for i in range (X_train.shape[0]):

            num = num + ((X_train[i] - X_train.mean())*(Y_train[i] - Y_train.mean()))
            den = den + ((X_train[i] - X_train.mean())*(X_train[i] - X_train.mean()))

        self.coef_ = num/den
        
        if self.fit_intercept:
            
            self.intercept_ = (Y_train.mean()) - ((self.coef_)*(X_train.mean()))
        
        else :
            
            self.intercept_ = 0
            
        if self.positve:
           
            self.coef_ = abs(coef_)
            self.intercept_ = abs(intercept_)

    def predict(self , X_test):

        for i in range(X_test.shape[0]):
      
            prediciton = self.intercept_ + (self.coef_ * X_test[0])
      
            self.pre.append(prediciton)
    
        return self.pre
