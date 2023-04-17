features = np.array([x for x in range(0 , 200 , 1)])
target = []
for i in range(200):
    if i < 26:
        target.append(i**(1 / 2))
    else :
        target.append(i**(1/3))
target = np.array(target)
weights = np.random.randn(1)
biases = np.random.randn(1)
pred = weights * 30 + biases
loss = (pred - 60)
weights -= ((-2* (60 - weights*30 - biases)) + (2 * weights)) * 0.01
