def SGDRegressor():
    weights = abs(np.random.randn(1))
    biases = abs(np.random.randn(1))
    predic = []
    losses = []
    for _ in range(300):
        pred = weights * features + biases
        loss = np.sum((pred - target) ** 2)
        losses.append(loss)
        weights -= -2 * loss * 0.01
        biases -= -2 * 30 * loss * 0.01

    return weights , biases
