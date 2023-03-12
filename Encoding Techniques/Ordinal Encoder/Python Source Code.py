def ordinal_encoder(dataset , columns):
    
    for i in columns: 
    
      for j , k in zip(dataset[i].value_counts().index , 
                         range(len(dataset[i].value_counts().index))):
    
            dataset[i] = np.where(dataset[i] == j , k , data[i])
            
    return dataset
