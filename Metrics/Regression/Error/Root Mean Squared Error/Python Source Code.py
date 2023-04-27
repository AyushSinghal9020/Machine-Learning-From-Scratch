def mean_squared_error(actuals , predictions):
    
    error = 0
    
    for prediction , actual in zip(predictions , actuals):
            
        error += (actual - prediction) ** 2
    
    return (error/len(predictions)) ** (1 / 2)
