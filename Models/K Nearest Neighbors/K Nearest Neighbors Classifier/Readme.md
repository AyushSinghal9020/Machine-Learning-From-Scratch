# K Nearest Neighbors Classifier 

The K Nearest Neighbors (KNN) algorithm is a type of supervised machine learning algorithm used for classification and regression tasks. In classification tasks, KNN predicts the class label of a new data point based on the class labels of the K nearest training data points.

The KNN algorithm is simple to understand and implement, making it a popular choice for classification tasks. To classify a new data point, KNN first calculates the distance between the new data point and all the training data points. It then selects the K training data points that are closest to the new data point based on the distance metric.

Once the K nearest neighbors have been identified, KNN assigns the new data point to the class that is most common among its K nearest neighbors. For example, if the K nearest neighbors are three red points and two blue points, KNN will classify the new data point as red.

The choice of K is a crucial hyperparameter in KNN, as it determines the number of neighbors that will be considered when making predictions. A small value of K may result in overfitting, while a large value of K may result in underfitting. Therefore, it is essential to choose an appropriate value of K for the given problem.

Overall, KNN is a versatile algorithm that can be used for both classification and regression tasks, and it is a good choice when the dataset is small and the number of features is low. However, it can become computationally expensive when dealing with large datasets.

**Modules Used**
* Numpy 
* Pandas 
* Counter
* Matplotlib
