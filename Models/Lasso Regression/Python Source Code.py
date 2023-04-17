def LassoRegression(X , y , alpha = 0.1):
    
    weights = np.random.randn(X.shape[0])
    biases = np.random.randn(1)
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        
        loss = np.sum((y - (weights * X + biases)) + (alpha * weights))
        losses.append(loss)
        
        weights -= ((-2* loss) + alpha) * 0.01
        biases -= -2 * loss * 0.01

    return weights , biases
