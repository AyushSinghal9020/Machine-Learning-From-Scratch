# Mean Sqaured Error

Mean Squared Error (MSE) is a widely used metric in machine learning to measure the quality of a regression model. It is calculated as the average of the squared differences between the predicted and actual values of the target variable.

MSE measures the average squared distance between the predicted and actual values, which gives a rough idea of how far off the predictions are from the actual values. A smaller MSE indicates that the model is making more accurate predictions, whereas a higher MSE suggests that the model is not performing well.

MSE is a popular metric because it is easy to understand and calculate, and it is useful in situations where the goal is to minimize the average squared error. However, it has some limitations, such as being sensitive to outliers and not giving equal weight to all data points.

In summary, MSE is a useful metric in evaluating regression models and can provide insights into the model's accuracy. However, it is essential to consider other metrics and the context of the problem to get a complete picture of the model's performance.

****
$$\frac {1}{n}\sum\limits_{i = 1}^{n}(y - \hat y)^2$$
****
