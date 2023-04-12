for i in sample_data.value_counts().index:
    sample_data["MSZoning" + "_" + i[0]] = np.where(sample_data["MSZoning"] == i[0] , 1 , 0)
    
sample_data.drop("MSZoning" + "_" + str(sample_data["MSZoning"].value_counts().index[0]) , axis = 1 , inplace = True)
