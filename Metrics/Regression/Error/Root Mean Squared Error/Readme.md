# Root Mean Sqaured Error

Root Mean Squared Error (RMSE) is a commonly used evaluation metric in regression analysis that measures the average magnitude of the errors between the predicted and actual values. RMSE is the square root of the mean of the squared differences between the predicted and actual values, and it is expressed in the same units as the target variable.

A lower RMSE value indicates that the model has better accuracy in predicting the target variable. RMSE is a popular metric for evaluating regression models because it penalizes larger errors more severely than smaller errors, making it sensitive to outliers and extreme values.

RMSE is widely used in various fields such as finance, economics, and engineering to evaluate the accuracy of models predicting continuous variables like stock prices, sales, or demand. However, it is important to note that RMSE is not the only metric used in regression analysis and should be used in conjunction with other metrics like Mean Absolute Error (MAE) or R-Squared (R^2) for a more comprehensive evaluation of the model's performance.

****
$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}(y - \hat y)^2}$$
****
