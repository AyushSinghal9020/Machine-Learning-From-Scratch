def min_max_scaler(array , copy = True):
    
    if copy:
        
        y = np.empty(shape = array.shape)
        
        for i,j in enumerate(array):
            
            y[i] = (j - array.min()) / (y.max() - y.min())
        
        return y
    
    else :
        
        for i,j in enumerate(array):
            
            array[i] = (j - array.min()) / (array.max() - array.min())
        
        return array
