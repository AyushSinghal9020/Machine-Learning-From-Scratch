features = np.array([x for x in range(0 , 200 , 1)])
target = []
for i in range(200):
    if i < 26:
        target.append(i**(1 / 2))
    else :
        target.append(i**(1/3))
target = np.array(target)
