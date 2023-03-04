def log(value):
    
    return np.log1p(value)

def square(value):
    
    return np.sqaure(value)

def yeo_johnson(value , lambdas):
    
    if value >= 0:
    
        if lambdas == 0:
    
            return (np.log1p(value))
    
        else:
    
            return ((((value + 1) ** lambdas) - 1) / lambdas)
    
    if value < 0:
    
        if lambdas == 2: 
    
            return (-np.log1p(-value))
    
        else : 
    
            return ((- ((((- value) + 1) ** 2 - lambdas) - 1)) / (2 - lambdas))

def box_cox(value , lambdas):

    if lambdas == 0:

        return np.log1p(value)

    else :

        return ((((value + 1) ** lambdas) - 1) / lambdas)

def function_transformer(array , func = None):

    if func == None:
        print("Please enter a function")
        return None

    elif func == "log" or func == "square":

        output_array = np.empty(shape = array.shape)

        if len(array.shape) == 1:
            new_array = np.empty(shape = (1 , 1))
            for i in array:

                if func == "log":

                    new_array = np.vstack([new_array , log_output(i)])
                
                else:
                    
                    new_array = np.vstack([new_array , square(i)])
            
            new_array = np.delete(new_array , 0 , 0)

            return new_array

        else :
            
            for i in array:
            
                new_array = np.empty(shape = (1 , 1))
            
                for j in array[i]:
            
                    if func == "log":

                        new_array = np.vstack([new_array , log_output(i)])
                    else:
                    
                        new_array = np.vstack([new_array , square(i)])

                new_array = np.delete(new_array , 0 , 0)

                output_array = np.hstack([output_array , new_array])
                output_array = np.delete(output_array , 0 , 1)

            return output_array
    
    elif func == "box_cox" or func == "yeo_johnson":
        
        output_array = np.empty(shape = array.shape)

        if len(array.shape) == 1:

            array_list = []
            skew_list = []
            
            for constant in range(-5 , 5):
            
                new_array = np.empty(shape = (1 , 1))

                for values in array:

                    if func == "box_cox":

                        new_array = np.vstack([new_array , box_cox(values , constant)])

                    else :
                        new_array = np.vstack([new_array , yeo_johnson(values , constant)])
                
                new_array = np.delete(new_array , 0 , 0)
                
                array_list.append(new_array)
                skew_list.append(pd.DataFrame(new_array).skew()[0] ** 2)

                output_array = array_list[np.argmin(skew_list)]
            
            return output_array

        elif len(array.shape) != 1:

            for columns in array:

                array_list = []
                skew_list = []
                
                for constant in range(-5 , 5):
                    
                    new_array = np.empty(shape = (1 , 1))

                    for values in array[columns]:

                        if func == "box_cox":

                            new_array = np.vstack([new_array , box_cox(values , constant)])

                        else :
                            
                            new_array = np.vstack([new_array , yeo_johnson(values , constant)])

                    new_array = np.delete(new_array , 0 , 0)
                    
                    array_list.append(new_array)
                    skew_list.append(pd.DataFrame(new_array).skew()[0] ** 2)

                    output = array_list[np.argmin(skew_list)]

                output_array = np.hstack([output_array , output])

                output_array = np.delete(output_array , 0 , 1)

            return output_array

        else :
            print("Please enter a valid input")

    else :
        print("Please enter a valid function")
        return None
