def standard_scaler(array):
    
    scaled = np.array([])

    for i in range(len(array.shape)) : 
    
        single_scaled = np.array([])
        
        if len(array.shape) == 1:
                
            if not (array.dtype == int or array.dtype == float) :

                print(i , "th index was a categorical column, Please pass only numerical columns. ")
                
            else:    
                
                for j in array:
                
                    scale = (j - array.mean())/ array.std()

                    single_scaled = np.hstack([single_scaled , scale])
                    
                scaled = single_scaled
        
        else:
    
            for j in array[i]:

                if not (array[i].dtype == int or array[i].dtype == float) :

                    print(i , "th index was a categorical column, Please pass only numerical columns. ")
                    scaled = np.zeros(len(array[i]))

                else:

                    scale = (j - array[i].mean())/ array[i].std()

                    single_scaled = np.hstack([single_scaled , scale])

            scaled = np.vstack(scaled . single_scaled)

    return scaled
