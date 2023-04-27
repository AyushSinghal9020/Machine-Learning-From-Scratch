# Max Error

Max Error is a metric used in machine learning to evaluate the performance of a model in predicting continuous numerical values. It measures the maximum difference between the predicted values and the actual values in the test set. In other words, Max Error represents the largest deviation between the predicted and true values.

Max Error is useful in applications where the accuracy of the model's predictions is critical, such as in financial modeling or scientific simulations. A high Max Error score indicates that the model has a large deviation between predicted and actual values, and it may need to be improved. On the other hand, a low Max Error score indicates that the model's predictions are very close to the actual values, and it is performing well.

It is important to note that Max Error is a very sensitive metric and is heavily influenced by outliers in the dataset. Therefore, it should not be used as the sole criterion to evaluate the performance of a model. It should be used in conjunction with other metrics such as mean squared error (MSE), mean absolute error (MAE), or root mean squared error (RMSE) to get a more comprehensive understanding of the model's performance.

****
$$error = max(y - \hat y)$$
****
