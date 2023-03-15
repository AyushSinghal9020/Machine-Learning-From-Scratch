# Ridge Regression

`Ridge regression` is a type of `linear regression` that is used to `deal` with `multicollinearity`. An `additional penalty term` is `added` to the `cost function` in order to `shrink` the `coefficients` of the `predictor variables` towards `zero`.

The `strength` of the `penalty term` is controlled by a `hyperparameter` $λ$. `Ridge regression` can be used in situations where there are `many predictor variables`, but the number of observations is relatively small. It can also be useful when there is multicollinearity among the predictor variables, which can lead to unstable coefficient estimates.

Ridge regression has several advantages over traditional linear regression, including reduced variance, improved stability of coefficient estimates, and the ability to handle multicollinearity. However, it also has some limitations, including the need to tune the hyperparameter λ and the possibility of introducing bias into the coefficient estimates if the penalty term is too strong.
$$J_{\beta_-modified} = RSS_\beta + \lambda \sum\beta^2$$

$$\beta_{Ridge} = \frac {x^Ty}{x^TX+\lambda}$$
