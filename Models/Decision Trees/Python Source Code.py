class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        
        self.min_samples_split=min_samples_split
        self.max_depth=max_depth
        self.n_features=n_features
        self.root=None
        
    def fit(self , X , y):pass
    
    def _best_split(self, X, y, feat_idxs):
        
        best_gain = -1
        split_idx, split_threshold = None, None

        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)

            for thr in thresholds:
                
                gain = self._information_gain(y, X_column, thr)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = thr

        return split_idx, split_threshold
    
    def _information_gain(self, y, X_column, threshold):

        parent_entropy = self._entropy(y)

        left_idxs, right_idxs = self._split(X_column, threshold)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        child_entropy = (len(left_idxs)/len(y)) * (self.entropy(y[left_idxs])) + (len(right_idxs)/len(y)) * (self._entropy(y[right_idxs]))

        information_gain = parent_entropy - child_entropy
        return information_gain
    
    entropy = lambda self , y : -np.sum(np.array([p * np.log(p)
                                                 for p in (np.bincount(y) / len(y))]))
    
    def split(self, X_column, split_thresh):
        
        left = np.argwhere(X_column <= split_thresh).flatten()
        right = np.argwhere(X_column > split_thresh).flatten()
        
        return left , right
    
    def predict(self , X):pass
