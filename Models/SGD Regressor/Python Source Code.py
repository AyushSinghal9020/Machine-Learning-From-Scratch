features = np.array([x for x in range(0 , 200 , 1)])
target = np.array([x for x in range(0 , 400 , 2)])
weights = abs(np.random.randn(1))
biases = abs(np.random.randn(1))
losses = []
for _ in range(100):
    weights -= -2 * loss * 0.01
    biases -= -2 * 30 * loss * 0.01
    loss = (60 - (weights * 30 + biases))
    losses.append(loss)
