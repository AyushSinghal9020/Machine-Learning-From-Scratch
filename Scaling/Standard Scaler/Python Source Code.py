y = np.empty(shape = (100))
for i,j in enumerate(x):
    y[i] = (j - x.mean()) / (x.std())
