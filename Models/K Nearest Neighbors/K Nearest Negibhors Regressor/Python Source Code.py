class KNeighborsRegressor():
  
  def __init__(self , k):
    
    self.k = k
  
  def fit(self , X_train , Y_train):
    
    self.X_train = X_train
    self.Y_train = Y_train

  def predict(self , X_train):
    
    prediction = []

    for i in range(X_train.shape[0]):

      distances = np.sum((self.X_train - X_train[i])**2 , axis = 1)
      
      nearest_indices = np.argsort(distances)[:self.k]
      nearest_labels = self.y_train[nearest_indices]
      
      prediction = np.mean(nearest_labels)
      prediction.append(prediction)

    return np.array(prediction)
