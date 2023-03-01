## Min Max Scaling 
Min-max scaling is a common data preprocessing technique used in machine learning to scale numerical features of a dataset to the range 0 to 1.

To perform min-max scaling, the minimum and maximum values ​​of the features are first determined. Then, for each value of the feature, the difference between value and minimum is divided by the range (that is, the difference between maximum and minimum). This scales the minimum value to 0, the maximum value to 1, and proportionally scales all other values ​​in between.

Min-max scaling is useful when the range of values ​​for different features is large and can have a large impact on the learning algorithm. Scaling all features to the same range prevents features with large values ​​from dominating the learning process and ensures that all features are equally important.

Note that min-max scaling does not change the distribution of the data. So if the original data is skewed or has outliers, those features will still be there after scaling. If the new data contains values ​​outside the original range, scaling may not work as expected. 

The basic formula behind min-max scaling is
**** 

$$x_{sclaed} = \frac {x_{i} - x_{min}}{x_{max} - x_{min}}$$
****
