def LassoRegression(X , y , 
                    alpha = 0.1 , fit_intercepts = True):
    
    weights = np.zeros(shape = X.shape[0])
    biases = np.zeros(shape = (1))
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        
        loss = np.sum((y - (weights * X + biases)) + (alpha * weights))
        losses.append(loss)
        
        weights -= ((-2* loss) + alpha) * 0.01
        
        if fit_intercept:
                      
            biases -= -2 * loss * 0.01

    return weights , biases
