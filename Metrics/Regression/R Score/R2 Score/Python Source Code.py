def mean_squared_log_error(actuals , predictions):
    
    error = 0
    
    for prediction , actual in zip(predictions , actuals):
            
        error += ((actual - prediciton) / (actual - predicitons.mean())) ** 2
    
    return 1 - error
