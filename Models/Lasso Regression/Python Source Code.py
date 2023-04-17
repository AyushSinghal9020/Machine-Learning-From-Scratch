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
for _ in range(100):
    weights -= ((-2* loss) + 1) * 0.01
    biases -= -2 * 30 * loss * 0.01
    loss = (60 - (weights * 30 + biases)) + (weights)
