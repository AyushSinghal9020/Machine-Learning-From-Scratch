def f_1_score_micro(predictions , actuals):

    metrics = np.empty(shape = (2 , len(np.unique(pred)) + 1))
    
    for uniques in range(len(np.unique(pred))):
        
        x = np.empty(shape = (3))
        
        trues = 0
        falses = 0
        
        for actu , predi in zip(act , pred):
            
            if ((actu == np.unique(pred)[uniques]) and (predi == np.unique(pred)[uniques])):
            
                trues += 1
            
            else :
            
                falses += 1
        
        x[0] = uniques
        x[1] = trues
        x[2] = falses
        
        metrics[i] = x
    
    recall = []
    
    if metrics.shape[0] == 2:
    
        recall.append(metrics[0][1] / (metrics[0][1] + ((1 / 2) * (metrics[0][2] + metrics[1][2]))))
        recall.append(metrics[1][1] / (metrics[1][1] + ((1 / 2) * (metrics[0][2] + metrics[0][2]))))
    
    else :
    
        for labels in range(len(metrics)): 
            x = [x[2] for x in range(metrics.shape[0])]
            # Changed the formula here
            recall.append(metrics[labels][1] / (metrics[labels][1] + ((1 / 2) * np.sum(np.array(x)))))
    
    return np.sum(np.array(recall))
