def PCA(array , n_components):
    mean = array - np.mean(array)
    cov = np.cov(mean.T)
    
    _ , eigen_vectors = np.linalg.eig(cov)
    
    idx = np.argsort(eigen_vectors)
    eigen_vectors = eigen_vectors[idx]
    
    components = eigen_vectors[0 : n_components]
    
    return np.dot(mean , components.T)
