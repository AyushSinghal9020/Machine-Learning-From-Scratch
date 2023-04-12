def sample_func(dataframe , columns):
    
    if len(columns) == 1 :
        
        for i in columns:
                
            for j in dataframe[i].value_counts().index[0]:
                
                dataframe[i + "_" + j[0]] = np.where(dataframe[i] == j[0] , 1 , 0)
                
            dataframe.drop(i , axis = 1 , inplace = True)

    else : 
        
        for i in columns:
                
            for j in dataframe[i].value_counts().index[0]:
                
                dataframe[i + "_" + j] = np.where(dataframe[i] == j , 1 , 0)
                
            dataframe.drop(i , axis = 1 , inplace = True)
