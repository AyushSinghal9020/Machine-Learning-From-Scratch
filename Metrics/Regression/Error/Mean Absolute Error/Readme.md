# Mean Absolute Error

Mean Absolute Error (MAE) is a commonly used metric in machine learning to evaluate the accuracy of a regression model. It measures the average absolute difference between the predicted and actual values of the target variable.

MAE is a simple and intuitive metric that is easy to understand and interpret. It provides a measure of how far off the predictions are on average, regardless of whether they are overestimating or underestimating the actual values. A lower MAE indicates that the model is making more accurate predictions.

One limitation of MAE is that it treats all errors equally, regardless of their magnitude. In some cases, the model may be making large errors for certain instances, which may be more important to the problem at hand. In such cases, Mean Squared Error (MSE) or Root Mean Squared Error (RMSE) may be more appropriate metrics to use.

Overall, MAE is a useful metric for evaluating the performance of regression models and can provide valuable insights into the model's accuracy.

****
$$\frac {1}{n}\sum\limits_{i = 1}^{n}|y - \hat y|$$
****
