class MultipleRidgeRegression():

  def __init__(self , alpha):
    self.coef = None
    self.interpet = None
    self.alpha = alpha

  def fit(self , X_train , Y_train):
    
    X_train = np.insert(X_train , 0 , 1 , axis = 1)
    I = np.identity(X_train.shape[1])
    result = np.linalg.inv(np.dot(X_train.T , X_train) + self.alpha*I).dot(X_train.T).dot(Y_train)
    self.intercept = result[0]
    self.coef = result[1:]

  def predict(self , X_test):

    Y_pred = np.dot(X_test.coef) + self.intercept

    return Y_pred
