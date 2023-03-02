def one_hot_encoder(dataframe , columns , min_frequency = None , max_categories = None):
    
    if min_frequency == None or max_categories == None :    
        
        if len(columns) == 1:

            for i in columns:
                    
                for j in dataframe[i].value_counts().index[0]:
                    
                    dataframe[i + "_" + j[0]] = np.where(dataframe[i] == j[0] , 1 , 0)
                    
                dataframe.drop(i , axis = 1 , inplace = True)

        else : 
        
            for i in columns:
                    
                for j in dataframe[i].value_counts().index[0]:
                    
                    dataframe[i + "_" + j] = np.where(dataframe[i] == j , 1 , 0)
                    
                dataframe.drop(i , axis = 1 , inplace = True)
        

    elif not min_frequency == None:
    
        if len(columns) == 1 :
            
            for i in columns:
                
                inf = [j 
                    for j in dataframe[i].value_counts().index 
                    if dataframe[i].value_counts()[j] > min_frequency]
            
                for j in dataframe[i].value_counts().index:
            
                    if not j in inf:
            
                        dataframe[i + "_" + j[0]] = np.where(dataframe[i] == j[0] , 1 , 0)
            
                    else: 
            
                        dataframe[i + "_other"] = np.where(dataframe[i].isin(inf) , 1 , 0)
            
                dataframe.drop(i , axis = 1 , inplace = True)
        else :
            for i in columns:
                
                inf = [j 
                    for j in dataframe[i].value_counts().index 
                    if dataframe[i].value_counts()[j] > min_frequency]
            
                for j in dataframe[i].value_counts().index:
            
                    if not j in inf:
            
                        dataframe[i + "_" + j] = np.where(dataframe[i] == j , 1 , 0)
            
                    else: 
            
                        dataframe[i + "_other"] = np.where(dataframe[i].isin(inf) , 1 , 0)
            
                dataframe.drop(i , axis = 1 , inplace = True) 

    elif not max_categories == None:
        
        if len(columns) == 1:

            for i in columns:
        
                inf = dataframe[i].value_counts().index[max_categories : ]
        
                for j in dataframe[i].value_counts().index[: max_categories]:
        
                    dataframe[i + "_" + j[0]] = np.where(dataframe[i] == j[0] , 1 , 0)
        
                dataframe[i + "_other"] = np.where(dataframe[i].isin(inf) , 1 , 0)
                dataframe.drop(i , axis = 1 , inplace = True)

        else :

            for i in columns:
        
                inf = dataframe[i].value_counts().index[max_categories : ]
        
                for j in dataframe[i].value_counts().index[: max_categories]:
        
                    dataframe[i + "_" + j] = np.where(dataframe[i] == j , 1 , 0)
        
                dataframe[i + "_other"] = np.where(dataframe[i].isin(inf) , 1 , 0)
                dataframe.drop(i , axis = 1 , inplace = True)
