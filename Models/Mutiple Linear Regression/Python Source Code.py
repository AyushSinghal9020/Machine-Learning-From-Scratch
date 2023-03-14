class MultipleLinearRegression():

  def __init__(self):
    self.coef = None
    self.interpet = None

  def fit(self , X_train , Y_train):
    
    np.insert(X_train , 0 , 1 , axis = 1)

    betas = (np.linalg.inv(np.dot(X_train.T , X_train))).dot(X_train.T).dot(Y_train)
    
    self.intercept = betas[0]
    self.coef = betas[1:]
  
  def predict(self , X_test):

    Y_pred = np.dot(X_test.coef) + self.intercept

    return Y_pred
