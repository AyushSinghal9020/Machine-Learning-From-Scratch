<a href="https://www.kaggle.com/code/ayushs9020/knn-from-scratch"><img src = "https://cdn.iconscout.com/icon/free/png-256/free-kaggle-3521526-2945029.png" width = 50>

# K Nearest Neighbors

K Nearest Neighbors (KNN) is a popular machine learning algorithm used for both classification and regression tasks. It is a non-parametric method that makes predictions based on the similarity between input samples. The KNN algorithm is considered a lazy learner because it does not explicitly build a model during the training phase but instead stores the entire training dataset in memory. The basic idea behind KNN is to classify or predict the target value of a new data point based on its proximity to the labeled data points in the feature space. In other words, the algorithm assumes that similar instances should have similar output values. The "K" in KNN refers to the number of neighbors considered when making predictions.

The choice of the parameter K is crucial in KNN. A smaller value of K makes the model more sensitive to noise and may result in overfitting, whereas a larger value of K may lead to oversimplification and loss of important patterns in the data. KNN has several advantages, such as simplicity and interpretability. It can be used for both classification and regression tasks and can handle multi-class problems. Additionally, KNN does not make any assumptions about the underlying data distribution, which makes it applicable to a wide range of scenarios. However, KNN can be computationally expensive, especially when dealing with large datasets, as it requires calculating distances between the new point and all training points.

$$distance = \sqrt{(x_1 - x_2)^2 + (y_2 - y_1)^2 + ... + (n_1 - n_2)^2}$$
