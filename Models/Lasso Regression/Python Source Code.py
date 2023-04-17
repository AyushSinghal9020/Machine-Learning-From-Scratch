class LassoRegression:
    
    def __init__(self , X , y , 
                    alpha = 0.1 , fit_intercept = True):pass
    
    def fit(self , X , y , sample_weight): 
        
        if sample_weight != None:
            
            if len(sampe_weight) != (X.shape[0] + 1):
            
                warnings.warn("Please use the correct shape of `sample_weights`. using `0` as the parameters!!")
            
            else : 
                
                weights , biases = sample_weight[:1] , sample_weight[0]
        
        else : 
        
            weights = np.zeors(shape = X.shape[0])
            biases = np.zeors(1)
    
        predic = []
        losses = []

        for _ in range(300):

            pred = weights * features + biases

            loss = np.sum((y - (weights * X + biases)) + (alpha * weights))
            losses.append(loss)

            weights -= ((-2* loss)) + alpha

            if fit_intercept:

                biases -= -2 * loss * 0.01

        return weights , biases
