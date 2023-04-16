# From Scratch Using Numpy

import numpy as np 

squared_mean = lambda predictions , actuals : np.sum((predictions - actual) ** 2)

def huber_loss(prediction , actuals , delta):
    
    loss = 0
    
    for pred , act in zip(predictions , actuals):
    
        if abs(pred - act) <= delta:
        
            loss += (1 / 2) * pred - act
        
        else :
        
            loss += (delta * abs(pred - act)) - ((1 / 2) * (delta ** 2))
    
    return loss

epsilon_intensive = lambda predictions , actuals , epsilon : np.where((predictions - actuals) < epsilon , 0 , (predictions - actuals))

def SGDRegressor(X , y , 
                 loss_type = "sqaured_mean" , delta = 0.2 , 
                 epsilon = 0 , alpha = 0.0001 , 
                fit_intercept = True , max_iter = 1000 , 
                shuffle = False , early_stopping = False):
    
    weights = np.zeors(shape = X.shape[0])
    biases = np.zeors(1)
    
    predic = []
    losses = []
    
    for epochs in range(max_iter):
        
        if shuffle :
        
            X = np.random.shuffle(x)
    
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

    return weights , biases

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
