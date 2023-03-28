def SGD(X_train , Y_train , epochs = 100 , lr = 0.01):
    
    def initialize(number_of_features):
    
        weights = np.random.randn(number_of_features) * 0.1
        biases = np.random.randn(1) * 0.1

        params = np.array([weights , biases])

    def predict(weights , biases , X_test):
        
        predicted_values = (weights * X_test) + biases

        return predicted_values

    def backward(Y_train , predicted):
    
        loss = (Y_train - predicted) ** 2
    
        return loss
    
    def forward(X_train , Y_train , epochs , lr):
    
        initialize(number_of_features)
    
        for _ in range(epochs):
    
            predict(weights , biases , X_train)
            backward(Y_train , predicted_values)
    
            weights = weights - (lr * loss)
            biases = biases - (lr * loss)

    forward(X_train , Y_train , epochs , lr)

    new_params = np.array([weights , biases])

    return new_params
