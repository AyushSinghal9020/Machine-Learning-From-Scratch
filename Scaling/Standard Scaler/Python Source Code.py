def standard_scaler(array , copy = True):
    if copy:
        
        y = np.empty(shape = array.shape)
        
        for i,j in enumerate(array):
            
            y[i] = (j - array.mean()) / (array.std())
        
        return y
    
    else :
        
        for i,j in enumerate(array):
            
            array[i] = (j - array.mean()) / (array.std())
        
        return array
