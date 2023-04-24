def top_k_accuracy(actuals , predictions):
    
    correct_ones = 0
    
    for actual  , predicted in zip(actuals , predictions):
        
        if predicted == actual:
            
            correct_ones += 1

    asc = correct_ones / len(predictions)

    return asc
