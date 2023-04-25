def precision(actuals , predictions , k):
    
    k_labels = []
    
    for label in np.unique(pred):
        
        correct_ones = 0

        for actual  , predicted in zip(actuals , predictions):

            if predicted == label and actual == label:

                correct_ones += 1
            # Else condition here 
            else :
                
                false_ones += 1
        
        asc = correct_ones / false_ones
        
        k_labels.append(asc)

    k_labels = np.array(k_labels)
    
    return K_lables    
