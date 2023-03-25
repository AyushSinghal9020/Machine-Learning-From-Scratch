import numpy as np 

def cross_validation(model , dataframe , target , metric , times = 10):
    lis = []
    
    def pre(dataframe):
        x = dataframe.drop(target , axis = 1)
        y = dataframe[target]

        return x , y

    for _ in target:

        train , test = np.split(dataframe.sample(frac = 1) , [int(0.8 * len(dataframe))])

        X_train , Y_train = pre(train)
        X_test , Y_test = pre(test)

        model = model
        model.fit(X_train , Y_train)
        lis.append(metric(Y_test , model.predict(X_test))) 

    return np.array(lis).mean()  
