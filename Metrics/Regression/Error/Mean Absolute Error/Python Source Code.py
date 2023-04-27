def mean_absolute_error(actuals , predictions):
    
    error = 0
    
    for prediction , actual in zip(predictions , actuals):
            
        error += abs(actual - prediction)
    
    return error/len(predictions)
