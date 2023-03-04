def box_cox(value , lambdas):
    if lambdas == 0:
        return np.log1p(value)
    else :
        return ((((value + 1) ** lambdas) - 1) / lambdas)



output_array = np.empty(shape = sample_data.shape)

if len(sample_data.shape) == 1:

    array_list = []
    skew_list = []
    
    for i in range(-5 , 5):
    
        new_array = np.empty(shape = (1 , 1))

        for j in sample_data:

            new_array = np.vstack([new_array , box_cox(j , i)])

        new_array = np.delete(new_array , 0 , 0)
        
        array_list.append(new_array)
        skew_list.append(pd.DataFrame(new_array).skew()[0] ** 2)

        output_array = array_list[np.argmin(skew_list)]
elif len(sample_data.shape) != 1:
    
    for k in sample_data:

        array_list = []
        skew_list = []
        
        for i in range(-5 , 5):
            
            new_array = np.empty(shape = (1 , 1))

            for j in sample_data[k]:

                new_array = np.vstack([new_array , box_cox(j , i)])

            new_array = np.delete(new_array , 0 , 0)
            
            array_list.append(new_array)
            skew_list.append(pd.DataFrame(new_array).skew()[0] ** 2)

            output = array_list[np.argmin(skew_list)]

        output_array = np.hstack([output_array , output])

        output_array = np.delete(output_array , 0 , 1)
