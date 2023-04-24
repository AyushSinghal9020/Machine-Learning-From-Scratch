def average_precision_score(actuals , predictions):
    
    correct_ones = 0
    false_ones = 0
    
    for actual  , predicted in zip(actuals , predictions):
        
        if predicted == actual:
            
            correct_ones += 1
        
        else:
            
            false_ones += 1
            
    aps = correct_ones / false_ones

    return aps
