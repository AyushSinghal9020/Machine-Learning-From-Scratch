### Z Score Normaliation / Standard Score Normalization 

In machine learning, a z-score scaler is a normalization technique used to standardize characteristics of a data set. The z-score scaler scales each feature to have a mean of 0 and a standard deviation of 1. This is accomplished by subtracting the feature mean from each data point and dividing by the feature standard deviation.

where mean is the mean of the features and standard deviation is the standard deviation of the features. The resulting Z-score represents the number of standard deviations from the mean of the data points. A positive z-score indicates that the data point is above the average, and a negative z-score indicates that the data point is below the average.

Using a z-score scaler is useful when working with features at different scales or units. Feature standardization allows the model to give equal weight to each feature, preventing features with larger values ​​from dominating the model's predictions. Z-score scalers are commonly used in many machine learning algorithms. B. k Nearest Neighbors, Logistic Regression, and Support Vector Machines. 
****
$$x_{scaled} = \frac {x_{i} - x_{mean}}{\sigma}$$
$$\sigma = \frac {\sum (x_{i} - x_{mean})}{Number_-of_-values}$$
****
