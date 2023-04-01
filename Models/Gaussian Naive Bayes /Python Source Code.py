def gaussian(X_train , Y_train , Y_test):
  
    mean = np.empty(shape = (len(Y_train.unique())  , 
                             len(X_train.columns())))
    
    var = np.empty(shape = (len(Y_train.unique())  , 
                             len(X_train.columns())))
    
    
    for features in range(1 , len(X_train.columns) + 1):
    
        for classes in range(len(Y_train.unique())):
    
            mean[classes][features - 1] = data[data[0] == str(data[0].unique()[classes])][features].mean()
            var[classes][features - 1] = data[data[0] == str(data[0].unique()[classes])][features].var()

    output = np.zeros((len(Y_train.unique())))

    for feature in range(len(Y_train.unique())):
    
        for classess in range(len(X_train.columns) - 2):
    
            output[feature] += (np.exp(-(np.square(test[classess] - mean[classess][feature])) / (2 * var[classess][feature]))) * (1 / (np.sqrt(2 * 3.14 * np.square(var[classess][feature]))))

    output = np.sort(output)

    return output[-1]
