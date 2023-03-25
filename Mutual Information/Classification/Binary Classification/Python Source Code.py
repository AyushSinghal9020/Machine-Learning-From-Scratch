def binary_mi(dataframe , target , features):

    mi_list = []

    if len(dataframe[target].value_counts.index) > 2:
        
        print("Please enter binary values")
    
    else :
       
        for feature in features:
    
            if len(dataframe[feature].value_counts.index) > 2:
                
                print("Please enter binary values")
            
            else :
            
                outcome_matrix = np.zeros(shape = (3 , 3))
            
                for indices in range(dataframe.shape[0]):
                    
                    if dataframe[target][indices] == dataframe[target].value_counts.index[0]:
                    
                        if dataframe[feature][indices] == dataframe[target].value_counts.index[0]: 
                    
                            outcome_matrix[0 , 0] += 1
                    
                        else : 
                    
                            outcome_matrix[0 , 1] += 1
                    
                    else : 
                    
                        if dataframe[feature][indices] == dataframe[target].value_counts.index[1]:
                    
                            outcome_matrix[1 , 1] += 1
                    
                        else :
                    
                            outcome_matrix[1 , 0] += 1
                
                probablity_matrix = outcome_matrix / data.shape[0]
                
                for first_index in range(2):
                    
                    for second_index in range(2):
                    
                        probablity_matrix[first_index , 2] += probablity_matrix[first_index , second_index]
                        probablity_matrix[2 , first_index] += probablity_matrix[second_index , first_index]
                
                mi = 0 
                
                for first_indices in range(2):
                    for second_indeices in range(2):
                        mi += (probablity_matrix[first_indices , second_indeices] * (np.log1p(probablity_matrix[first_indices , second_indeices] / (probablity_matrix[2 , second_indeices] * probablity_matrix[first_indices , 2]))))
        mi_list.append(mi) 

    return mi_list               
            
