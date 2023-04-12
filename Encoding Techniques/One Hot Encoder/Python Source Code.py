def sample_func(dataframe , columns , min_frequency = None , dtype = float):
    if type(min_frquency) == int:
        pass
    else : 
        min_frequnecy *= len(columns)

    if not min_frequency == None:
    
        if len(columns) == 1 :
                
            inf = [j 
                for j in dataframe[columne[0]].value_counts().index 
                if dataframe[columne[0]].value_counts()[j] > min_frequency]
        
            for j in dataframe[columne[0]].value_counts().index:
        
                if not j in inf:
        
                    dataframe[columne[0] + "_" + j[0]] = np.where(dataframe[columne[0]] == j[0] , 
                                                                  dtype(1) , dtype(0))
        
                else: 
        
                    dataframe[columne[0] + "_other"] = np.where(dataframe[columne[0]].isin(inf) , 
                                                                dtype(1) , dtype(0))
                if drop == "first" or drop == "if_binary":
                    dataframe.drop(str(columns[0]) + "_" + sample_data[columne[0]].value_counts.index[0] , 
                                   axis = 1 , inplace = True)
            dataframe.drop(i , axis = 1 , inplace = True)
        else :
            for i in columns:
                
                inf = [j 
                    for j in dataframe[i].value_counts().index 
                    if dataframe[i].value_counts()[j] > min_frequency]
            
                for j in dataframe[i].value_counts().index:
            
                    if not j in inf:
            
                        dataframe[i + "_" + j] = np.where(dataframe[i] == j , 
                                                          dtype(1) , dtype(0))

                    else: 
            
                        dataframe[i + "_other"] = np.where(dataframe[i].isin(inf) , 
                                                           dtype(1) , dtype(0))
                    if drop == "first" or drop == "if_binary" :
                        dataframe.drop(str(i) + "_" + sample_data[i].value_counts.index[0] , 
                                       axis = 1 , inplace = True)
                dataframe.drop(i , axis = 1 , inplace = True) 
    else :    
        
        if len(columns) == 1:
        
            for j in dataframe[columne[0]].value_counts().index[0]:
                
                dataframe[columne[0] + "_" + j[0]] = np.where(dataframe[columne[0]] == j[0] , 
                                                        dtype(1) , dtype(0))
            if drop == "first" or drop == "if_binary" :
                        dataframe.drop(str(i) + "_" + sample_data[i].value_counts.index[0] , 
                                       axis = 1 , inplace = True)
            dataframe.drop(columne[0] , axis = 1 , inplace = True)

        else : 
        
            for i in columns:
                    
                for j in dataframe[i].value_counts().index[0]:
                    
                    dataframe[i + "_" + j] = np.where(dataframe[i] == j , 
                                                      dtype(1) , dtype(0))
                if drop == "first" or drop == "if_binary" :
                        dataframe.drop(str(i) + "_" + sample_data[i].value_counts.index[0] , 
                                       axis = 1 , inplace = True)
                dataframe.drop(i , axis = 1 , inplace = True)
