def RidgeRegression(X , y , alpha = 0.1):
    
    weights = np.random.randn(X.shape[0])
    biases = np.random.randn(1)
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        
        loss = np.sum((60 - (weights * 30 + biases)) + (alpha * (weights ** 2)))
        losses.append(loss)
        
        weights -= ((-2* loss) + (2 * weights)) * 0.01
        biases -= -2 * 30 * loss * 0.01

    return weights , biases
