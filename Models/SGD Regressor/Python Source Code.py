squared_mean = lambda predictions , actuals : np.sum((predictions - actual) ** 2)

def huber_loss(prediction , actuals , delta):
    
    loss = 0
    
    for pred , act in zip(predictions , actuals):
    
        if abs(pred - act) <= delta:
        
            loss += (1 / 2) * pred - act
        
        else :
        
            loss += (delta * abs(pred - act)) - ((1 / 2) * (delta ** 2))
    
    return loss

epsilon_intensive = lambda predictions , actuals , epsilon : np.where((predictions - actuals) < epsilon , 0 , (predictions - actuals))

def SGDRegressor(X , y , 
                 loss_type = "sqaured_mean" , delta = 0.2 , 
                 epsilon = 0 , alpha = 0.0001 , 
                fit_intercept = True):
    
    weights = np.zeors(shape = X.shape[0])
    biases = np.zeors(1)
    
    predic = []
    losses = []
    
    for _ in range(300):
    
        pred = weights * features + biases
    
        if loss_type == "sqaured_mean":
        
            loss = squared_mean(pred , y , delta)
        
        elif loss_type == "huber" : 
            
            loss = huber(pred , y)
        
        else :
        
            loss = epsilon_intensie(pred , y , epsilon)
        losses.append(loss)
        
        weights -= -2 * loss * alpha
        if fit_intercept:
            biases -= -2 * 30 * loss * alpha

    return weights , biases
