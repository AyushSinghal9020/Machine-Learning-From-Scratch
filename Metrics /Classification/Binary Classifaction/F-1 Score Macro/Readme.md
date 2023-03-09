# F-1 Score Macro

The F1 score macro is a metric used to evaluate the performance of a multiclass classification model. It calculates the harmonic mean of the precision and recall for each class and then averages the result across all classes.

The F1 score macro provides an overall assessment of the model's ability to correctly classify all classes. It is particularly useful in cases where the classes are imbalanced, and the model may perform well on some classes but poorly on others. In such cases, the F1 score macro gives an unbiased estimate of the model's performance across all classes.

To calculate the F1 score macro, the precision and recall are first calculated for each class. The precision measures the proportion of true positives among all positive predictions, while the recall measures the proportion of true positives among all actual positives. The F1 score is then calculated as the harmonic mean of precision and recall. Finally, the F1 score macro is calculated by averaging the F1 scores across all classes.

In summary, the F1 score macro is a useful metric for evaluating the performance of a multiclass classification model. It takes into account the precision and recall of each class and provides an unbiased estimate of the model's performance across all classes.
