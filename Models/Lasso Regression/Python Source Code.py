def LassoRegression(X , y):
    
    weights = np.random.randn(X.shape[0])
    biases = np.random.randn(1)
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        
        loss = np.sum((y - (weights * X + biases)) + (weights))
        losses.append(loss)
        
        weights -= ((-2* loss) + 1) * 0.01
        biases -= -2 * loss * 0.01

    return weights , biases
