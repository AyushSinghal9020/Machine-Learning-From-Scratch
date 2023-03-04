# Box Cox Transformer

The Box-Cox transformation is a statistical technique commonly used in machine learning that transforms a non-normal dependent variable to a normal distribution. This transformation helps improve the performance of certain machine learning algorithms that assume a normal distribution of the input data.

The Box-Cox transformation applies a power transformation to the data, and the value of the power parameter determines the order and direction of the transformation. Optimal values ​​of performance parameters are usually estimated using maximum likelihood estimation or cross-validation.

The Box-Cox transformer is particularly useful in regression analysis, where the dependent variable is often assumed to be normally distributed. Box-Cox transformation of the dependent variable satisfies the normality assumption and improves the accuracy of the regression model.

Overall, the Box-Cox transformer is a useful tool in machine learning to transform non-normal data into a normal distribution, improve the performance of certain algorithms, and help satisfy statistical assumptions. 

 $$ x_λ = \displaystyle \Bigg[\frac {\frac {x^{\lambda} - 1}{λ}}{log (x) } \frac {if}{if} \frac {λ != 0}{λ = 0}\Bigg]$$

 Geneally we try to find the value of $\lambda$ which minimizes the skewness, $\lambda$ depends upon the data, but generally its value lies between -5 to 5
