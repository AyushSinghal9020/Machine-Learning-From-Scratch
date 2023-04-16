features = np.array([x for x in range(0 , 200 , 1)])
target = np.array([x for x in range(0 , 400 , 2)])
weights = np.random.randn(1)
biases = np.random.randn(1)
pred = weights * 30 + biases
loss = (pred - 60)
weights -= (-2* (60 - weights*30 - biases)) * 0.001
