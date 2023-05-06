! pip install numpy
! pip install collections

import numpy as np
from collections import Counter
 
def KNN(X_train , y_train , X_test):
    
    distance = [0] * X_train.shape[0]
    
    for columns in X_train.columns:
        
        for index in range(len(X_train[columns])):
            
            distance[index] += X_train[columns][index] - X_test[columns][index]
    
    distance = np.sqrt(np.array(distance))
    
    return Counter(y_test[np.argsort(distance)[:3]]).most_common()[0][0]
