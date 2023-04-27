# Root Mean Squared Log Error

Root Mean Squared Log Error (RMSLE) is an evaluation metric commonly used in machine learning to measure the difference between the predicted and actual values of a continuous variable. It is particularly useful when the target variable has a wide range of values and there is a significant difference between the magnitudes of the actual and predicted values.

RMSLE is calculated as the square root of the mean of the squared differences between the logarithms of the predicted and actual values. This transformation helps to penalize the model more severely for underestimating the values rather than overestimating them, which is often desirable in certain applications.

RMSLE is often used in applications such as sales forecasting, demand prediction, and web traffic analysis. It can be a useful metric for evaluating the performance of models that aim to predict a continuous variable with a significant range of values. However, it is important to note that RMSLE is just one of many metrics that can be used to evaluate a model's performance and should be used in combination with other metrics to get a more comprehensive understanding of the model's strengths and weaknesses.

****
$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}(log(y) - log(\hat y))^2}$$
some people also write this as 
$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}log(\frac {y}{\hat y})^2}$$
$$= \sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}2log(\frac {y}{\hat y})}$$
as $log(a) - log(b) = log(\frac {a}{b})$

and $log(a)^n = nlog(a)$
****
