def mean_squared_log_error(actuals , predictions):
    
    error = 0
    
    for prediction , actual in zip(predictions , actuals):
            
        error += (np.log1p(actual) - np.log1p(prediction)) ** 2
    
    return (error/len(predictions)) ** (1 / 2)
