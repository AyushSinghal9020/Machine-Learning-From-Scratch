# R2 Score

R2 score, also known as the coefficient of determination, is a statistical measure used to evaluate the performance of a regression model. It measures the proportion of variance in the dependent variable that is explained by the independent variables in the model.

R2 score ranges from 0 to 1, with a higher value indicating a better fit of the model to the data. A score of 0 means the model does not explain any variability in the dependent variable, while a score of 1 indicates that the model perfectly explains all the variability in the dependent variable.

R2 score is particularly useful in evaluating the performance of a model when comparing it with other models. However, it has some limitations, such as being sensitive to the number of independent variables and the distribution of the data. For instance, a high R2 score does not necessarily mean that the model is accurate, and it could still have overfit the data.

In summary, R2 score is a useful metric for evaluating the performance of regression models, but it should be used in combination with other metrics to get a more comprehensive understanding of the model's performance.

****
$$1 - \sum\limits_{i = 1}^{n}\frac{(y - \hat y)^2}{(y - \bar y)^2}$$
****
