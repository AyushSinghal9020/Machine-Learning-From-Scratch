The F1 Score is a widely used metric in machine learning that measures the balance between precision and recall. It is the harmonic mean of precision and recall, with values ranging between 0 and 1, where 1 represents perfect precision and recall.

The F1 Score Micro is a variant of the F1 Score that is often used when dealing with imbalanced datasets. In this variant, the precision and recall for each class are aggregated into a single precision and recall score for the entire dataset. This means that the F1 Score Micro considers all instances in the dataset equally, regardless of their class labels.

One advantage of using the F1 Score Micro is that it can be particularly useful in cases where the majority class dominates the dataset. By aggregating the precision and recall scores across all classes, the F1 Score Micro gives equal weight to all instances in the dataset, which can help to address this issue.

Overall, the F1 Score Micro is a useful metric for evaluating the performance of machine learning models on imbalanced datasets, particularly when there is a large class imbalance or when the majority class dominates the dataset.

$$f1_-score_-1 = \frac {True_-Positive}{True_-Positive + \frac {1}{2}(False_-Positive + False_-Negative)}$$ 
$$f1_-score_-0 = \frac {True_-Negative}{True_-Negative + \frac {1}{2}(False_-Positive + False_-Negative)}$$
