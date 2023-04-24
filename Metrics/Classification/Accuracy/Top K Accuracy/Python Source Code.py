def top_k_accuracy(actuals , predictions):
    
    k_labels = []
    
    for label in np.unique(pred):
        
        correct_ones = 0

        for actual  , predicted in zip(actuals , predictions):

            if predicted == label and actual == label:

                correct_ones += 1

        asc = correct_ones / len(predictions)
        
        k_labels.append(asc)

    return k_labels 
