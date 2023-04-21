# Balanced Accuracy Score
The balanced accuracy score is a performance metric used in binary classification problems, especially in cases where the distribution of classes is imbalanced. It is calculated as the average of the sensitivity and specificity of a classifier, where the sensitivity measures the proportion of positive instances correctly identified, and specificity measures the proportion of negative instances correctly identified.

Unlike the regular accuracy score, which can be misleading when dealing with imbalanced classes, the balanced accuracy score takes into account the imbalance of the classes and provides a more reliable measure of the classifier's performance.

The balanced accuracy score ranges from 0 to 1, where a score of 0 indicates a completely random classifier, and a score of 1 indicates a perfect classifier. A score of 0.5 indicates a classifier that performs no better than random chance.

Overall, the balanced accuracy score is a useful tool for evaluating the performance of classifiers in situations where the class distribution is imbalanced.
$$balanced_-accuracy_-score = \frac {sensitivity + specifictiy}{2}$$
