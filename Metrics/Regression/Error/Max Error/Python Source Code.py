def max_error(actuals , predictions):
    
    error = 0
    
    for prediction , actual in zip(predictions , actuals):
        
        if error < actual - prediction:
            
            error = actual - prediction
    
    return error
