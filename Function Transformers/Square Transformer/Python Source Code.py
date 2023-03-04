def log(value):
    return np.log1p(value)

def square(value):
    return np.sqaure(value)

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
    else:
        print("Please enter a valid function")
        return None
