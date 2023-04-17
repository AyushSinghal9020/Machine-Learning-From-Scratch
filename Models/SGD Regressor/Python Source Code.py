# From Scratch Using Numpy

import numpy as np 

class SGDRegressor:
    
    def __init__(self , loss_type = "sqaured_mean" , delta = 0.2 , 
                 epsilon = 0 , alpha = 0.0001 , 
                fit_intercept = True , max_iter = 1000 , 
                shuffle = False , early_stopping = False):
        
        pass
    
    def fit(self , X , y , sample_weight = None): 
    
        if sample_weight != None:
            
            if len(sampe_weight) != (X.shape[0] + 1):
            
                warnings.warn("Please use the correct shape of `sample_weights`. using `0` as the parameters!!")
            
            else : 
                
                weights , biases = sample_weight[:1] , sample_weight[0]
        
        else : 
        
            weights = np.zeors(shape = X.shape[0])
            biases = np.zeors(1)
            
        weights = []
        biases = []
        predic = []
        losses = []
        
        for epochs in range(max_iter):
            
            if shuffle :
            
                X = np.random.shuffle(X)
        
            pred = weights * X + biases
        
            if loss_type == "sqaured_mean":
            
                loss = squared_mean(pred , y , delta)
            
            elif loss_type == "huber" : 
                
                loss = huber(pred , y)
            
            else :
            
                loss = epsilon_intensie(pred , y , epsilon)
            
            losses.append(loss)
            
            if early_stopping: 
            
                if losses[epochs] == losses[epochs - 1]:
            
                    break
            
            weights -= -2 * loss * alpha
            
            if fit_intercept:
            
                biases -= -2 * 30 * loss * alpha
            
            weights_list.append(weights)
            biases_list.append(biases)
        
        weights_list = np.array(weights_list)
        biases_list = np.array(biases_list)

        return weights , biases

    def get_params(self , deep = True): 
        
        if deep:
            
            return weights_list , biases_list
        
        else :
        
            return weights , biases
    
    def predict(self , x_test):
        
        predictions = [np.sum(weghts * x + biases) for x in X_test]
        predictions = np.array(predictions)
        
        return predictions

    squared_mean = lambda predictions , actuals : np.sum((predictions - actual) ** 2)

    epsilon_intensive = lambda predictions , actuals , epsilon : np.where((predictions - actuals) < epsilon , 0 , (predictions - actuals))
    
    def huber_loss(prediction , actuals , delta):
        
        loss = 0
        
        for pred , act in zip(predictions , actuals):
        
            if abs(pred - act) <= delta:
            
                loss += (1 / 2) * pred - act
            
            else :
            
                loss += (delta * abs(pred - act)) - ((1 / 2) * (delta ** 2))
        
        return loss

# From Scratch Using Pytorch

import torch
import torch.nn as nn

def SGDR_pytorch(X , y , loss = "MSE" , alpha = 0.01 , fit_intercept = True , max_iter = 1000):
    
    if fit_intercept:
        
        model = nn.Linear(X.shape[0] , 1 , bias = False)
    
    else :
        
        model = nn.Linear(X.shape[0] , 1)
    
    optimizer = torch.optim.SGD(model.parameters() , alpha)
    
    if loss == "MSE":
        
        sample_loss = MSELoss()
    
    else :
        
        sample_loss = HuberLoss()
    
    for _ in range(max_iter):
        
        predicted = model(X)
        
        loss = sample_loss(predicted , y)
        
        loss.backward(retain_graph = True)
        optimizer.step()

        return model().detach().numoy()
