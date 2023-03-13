class LinearRegression():

  def __init__(self):
    self.m = None
    self.b = None
    self.pre = []

  def fit(self , X_train , Y_train):

    num = 0
    den = 0
    
    for i in range (X_train.shape[0]):

      num = num + ((X_train[i] - X_train.mean())*(Y_train[i] - Y_train.mean()))
      den = den + ((X_train[i] - X_train.mean())*(X_train[i] - X_train.mean()))

    self.m = num/den
    self.b = (Y_train.mean()) - ((self.m)*(X_train.mean()))

  def predict(self , X_test):

    for i in range(X_test.shape[0]):
      
      prediciton = self.b + (self.m * X_test[0])
      
      self.pre.append(prediciton)
    
    return self.pre
