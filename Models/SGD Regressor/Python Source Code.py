def SGDRegressor():
    weights = abs(np.random.randn(1))
    biases = abs(np.random.randn(1))
    predic = []
    losses = []
    for _ in range(300):
        pred = weights * features + biases
        predic.append(pred)
        loss = np.sum((pred - target) ** 2)
        losses.append(loss)
        weights += 0.000001 * loss
        biases += 0.000001 * loss

    return weights , biases
