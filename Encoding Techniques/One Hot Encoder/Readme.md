<a href="https://www.kaggle.com/code/ayushs9020/one-hot-encoder-from-scratch"><img src = "https://cdn.iconscout.com/icon/free/png-256/free-kaggle-3521526-2945029.png" width = 50>

# One Hot Encoding 
One-hot encoding is a technique used to convert categorical data into numerical data. It's called "one-hot" because each category is represented by a binary vector where all the elements are 0, except for one element which is 1, indicating the presence or absence of that category.

For example, suppose we have a column 'color' with three categories - red, blue, and green. We can represent red as [1,0,0], blue as [0,1,0], and green as [0,0,1]. When we have multiple columns of categorical data, we can apply one-hot encoding to each column separately.

The advantages of one-hot encoding include:

* Easy to implement and understand
* Can handle missing values
* Can be used for both continuous and categorical features
* Can be used as input to machine learning algorithms

However, there are some disadvantages too:

* Requires a large number of features for high-dimensional data
* May lead to the curse of dimensionality
* Not suitable for datasets with a large number of categories

To avoid these issues, we can use techniques such as label encoding, binary encoding, or even autoencoders. But one-hot encoding remains a popular choice due to its simplicity and ease of implementation.
