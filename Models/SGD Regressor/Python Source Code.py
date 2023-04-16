squared_mean = lambda predictions , actuals : np.sum((predictions - actual) ** 2)

def huber_loss(prediction , actuals):
    loss = 0
    for pred , act in zip(predictions , actuals):
        if abs(pred - act) <= 0.2:
            loss += (1 / 2) * pred - act
        else :
            loss += (0.2 * abs(pred - act)) - ((1 / 2) * (0.2 ** 2))
    return loss

def SGDRegressor(X , y , loss = "sqaured_mean"):
    
    weights = abs(np.random.randn(X.shape[0]))
    biases = abs(np.random.randn(1))
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
        if loss == "sqaured_mean":
            loss = squared_mean(pred , y)
        else : 
            loss = huber(pred , y)
        losses.append(loss)
        
        weights -= -2 * loss * 0.01
        biases -= -2 * 30 * loss * 0.01

    return weights , biases
