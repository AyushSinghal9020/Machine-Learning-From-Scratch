def RidgeRegression(X , y , 
                    alpha = 0.1 , fit_intercept = True):
    
    weights = np.zeors(shape = X.shape[0])
    biases = np.zeors(shape = 1)
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        
        loss = np.sum((60 - (weights * 30 + biases)) + (alpha * (weights ** 2)))
        losses.append(loss)
        
        weights -= ((-2* loss) + (2 * weights)) * 0.01
        
        if fit_intercept:
            
            biases -= -2 * 30 * loss * 0.01

    return weights , biases
