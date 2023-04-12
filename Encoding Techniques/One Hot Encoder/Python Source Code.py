def sample_func(dataframe , columns , drop = None):
    
    if len(columns) == 1 :
        
        for j in dataframe[columne[0]].value_counts().index[0]:

            dataframe[columns[0] + "_" + j[0]] = np.where(dataframe[columns[0]] == j[0] 
                                                          , 1 , 0)
        if drop == "first" :
            
            dataframe.drop(str(columns[0]) + "_" + sample_data[columne[0]].value_counts.index[0] , 
                          axis = 1 , inplace = True)

        dataframe.drop(columns[0] , axis = 1 , inplace = True)

    else : 
        
        for i in columns:
                
            for j in dataframe[i].value_counts().index[0]:
                
                dataframe[i + "_" + j] = np.where(dataframe[i] == j , 1 , 0)
            if drop == "first" :
            
                dataframe.drop(str(i) + "_" + sample_data[i].value_counts.index[0] , 
                               axis = 1 , inplace = True)
            
            dataframe.drop(i , axis = 1 , inplace = True)
