class OneHotEncoder:

    def __init__(self , min_frequency = None , max_categories = None , dtype = float):
        self.min_frequency = min_frequency
        self.max_categories = max_categories
        self.dtype = dtype
    def fit_transform(self , dataframe , columns):

        if type(self.min_frequency) == int:
            
            pass
        
        else : 
            
            self.min_frequency *= len(columns)

        if not self.min_frequency == None:
        
            if len(columns) == 1 :
                
                inf = [categories 
                    for categories in dataframe[columns[0]].value_counts().index 
                    if dataframe[columns[0]].value_counts()[categories] > self.min_frequency]
            
                for categories in dataframe[columns[0]].value_counts().index:
            
                    if not categories in inf:
            
                        dataframe[columns[0] + "_" + categories[0]] = np.where(dataframe[columns[0]] == categories[0] , dtype(1) , dtype(0))
            
                    else: 
            
                        dataframe[columns[0] + "_other"] = np.where(dataframe[columns[0]].isin(inf) , dtype(1) , dtype(0))
        
                    if drop == "first" or drop == "if_binary" :
        
                            dataframe.drop(str(columne[0]) + "_" + sample_data[columne[0]].value_counts.index[0] , 
                                        axis = 1 , inplace = True)
        
                    dataframe.drop(columne[0] , axis = 1 , inplace = True)
            else :
        
                for feature in columns:
                    
                    inf = [categories 
                        for categories in dataframe[feature].value_counts().index 
                        if dataframe[feature].value_counts()[categories] > self.min_frequency]
                
                    for categories in dataframe[feature].value_counts().index:
                
                        if not categories in inf:
                
                            dataframe[feature + "_" + categories] = np.where(dataframe[feature] == categories , dtype(1) , dtype(0))
                
                        else: 
                
                            dataframe[feature + "_other"] = np.where(dataframe[feature].isin(inf) , dtype(1) , dtype(0))
        
                        if drop == "first" or drop == "if_binary" :
        
                            dataframe.drop(str(feature) + "_" + sample_data[feature].value_counts.index[0] , 
                                        axis = 1 , inplace = True)
        
                    dataframe.drop(feature , axis = 1 , inplace = True) 

        elif not self.max_categories == None:
            
            if len(columns) == 1:
        
                inf = dataframe[columnes[0]].value_counts().index[self.max_categories : ]
        
                for categories in dataframe[columnes[0]].value_counts().index[: self.max_categories]:
        
                    dataframe[columnes[0] + "_" + categories[0]] = np.where(dataframe[columnes[0]] == categories[0] , dtype(1) , dtype(0))
        
                dataframe[columnes[0] + "_other"] = np.where(dataframe[columnes[0]].isin(inf) , dtype(1) , dtype(0))
        
                if drop == "first" or drop == "if_binary" :
        
                            dataframe.drop(str(columne[0]) + "_" + sample_data[columne[0]].value_counts.index[0] , 
                                        axis = 1 , inplace = True)
        
                dataframe.drop(columnes[0] , axis = 1 , inplace = True)

            else :

                for feature in columns:
            
                    inf = dataframe[feature].value_counts().index[self.max_categories : ]
            
                    for categories in dataframe[feature].value_counts().index[: max_categories]:
            
                        dataframe[feature + "_" + categories] = np.where(dataframe[feature] == categories , dtype(1) , dtype(0))
            
                    dataframe[feature + "_other"] = np.where(dataframe[feature].isin(inf) , dtype(1) , dtype(0))
        
                    if drop == "first" or drop == "if_binary" :
        
                            dataframe.drop(str(feature) + "_" + sample_data[feature].value_counts.index[0] , 
                                        axis = 1 , inplace = True)
        
                    dataframe.drop(feature , axis = 1 , inplace = True)

        else :    
            
            if len(columns) == 1:
                    
                for categories in dataframe[columns[0]].value_counts().index[0]:
                    
                    dataframe[columns[0] + "_" + categories[0]] = np.where(dataframe[columns[0]] == categories[0] , dtype(1) , dtype(0))
        
                if drop == "first" or drop == "if_binary" :
        
                            dataframe.drop(str(columns[0]) + "_" + sample_data[columns[0]].value_counts.index[0] , 
                                        axis = 1 , inplace = True)
        
                dataframe.drop(columns[0] , axis = 1 , inplace = True)

            else : 
            
                for feature in columns:
                        
                    for categories in dataframe[feature].value_counts().index[0]:
                        
                        dataframe[feature + "_" + categories] = np.where(dataframe[feature] == categories , dtype(1) , dtype(0))
        
                    if drop == "first" or drop == "if_binary" :
        
                            dataframe.drop(str(feature) + "_" + sample_data[feature].value_counts.index[0] , 
                                        axis = 1 , inplace = True)    
        
                    dataframe.drop(feature , axis = 1 , inplace = True)
