# One Hot Encoding 

One Hot Encoding is a popular technique used for categorical coding in machine learning. Convert a categorical variable to a binary format that can be used as input for a machine learning model.

This technique creates a separate binary feature for each category of a categorical variable. Each binary feature represents whether a category exists in the original data. For example, if you have three categories, A, B, and C, three binary features will be created, one for each category. If a data point belongs to category A, the category A binary characteristic has the value 1 and the categories B and C binary characteristics have the value 0.

One Hot Encoding is especially useful for nominal categorical variables that have no category-specific ordering. This technique ensures that machine learning models do not interpret the numbers associated with categories as having any inherent meaning or order.

The drawback of One Hot Encoding is that datasets with many categories have a large number of features, which can lead to computational resource problems and overfitting. Therefore, it is important to carefully consider using One Hot Encoding and use other techniques such as feature selection and dimensionality reduction if necessary. 
**Modules Used**
* Numpy 
* Pandas 

**Note**
* Pandas is only used to access the dataset at various levels
* The dataset used it [this ](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
