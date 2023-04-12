def sample_func(dataframe , columns):
    for i in columns:
                
        for j in dataframe[i].value_counts().index[0]:
                
            dataframe[i + "_" + j[0]] = np.where(dataframe[i] == j[0] , 1 , 0)
                
        dataframe.drop(i , axis = 1 , inplace = True)
