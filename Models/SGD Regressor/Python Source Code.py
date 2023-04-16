squared_mean = lambda predictions , actuals : np.sum((predictions - actual) ** 2)

def SGDRegressor(X , y):
    
    weights = abs(np.random.randn(X.shape[0]))
    biases = abs(np.random.randn(1))
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        
        loss = squared_mean(pred , y)
        losses.append(loss)
        
        weights -= -2 * loss * 0.01
        biases -= -2 * 30 * loss * 0.01

    return weights , biases
