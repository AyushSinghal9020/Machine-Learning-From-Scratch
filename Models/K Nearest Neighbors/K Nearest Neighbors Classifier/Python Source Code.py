class KNearestNeighborsClassifier():
  
    def __init__(self , k = 3):
  
        self.k = k

    def fit(self , X_train , Y_train):
  
        self.X_train = X_train
        self.Y_train = Y_train

    def predict(self , X_test):
  
        self.X_test = X_test
  
        predictions = [self.predict_proba(i) for i in X_test]
  
        return predictions

    def predict_proba(self , i):
  
        distances = [self.euc_dis(x , X_train) for X_train in self.X_train]
  
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.Y_train[i] for i in k_indices]
  
        most_commons = Counter(k_nearest_labels).most_common()
  
        return most_commons[0][0]

    euc_dis = lambda x1 , x2 : np.sqrt(np.sum(np.square(x1 - x2)))
