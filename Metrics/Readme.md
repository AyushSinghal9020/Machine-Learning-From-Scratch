<a href="https://www.kaggle.com/code/ayushs9020/metrics-from-scratch"><img src = "https://cdn.iconscout.com/icon/free/png-256/free-kaggle-3521526-2945029.png" width = 50>

# Metrics
Metrics in machine learning refer to the quantitative measurements used to evaluate the performance of a model. Metrics can be used to assess different aspects of a model's performance, such as accuracy, precision, recall, F1-score, AUC-ROC, and others. Choosing the right metrics for a given problem is important to ensure that the model's performance is appropriately evaluated and improved.

|Metrics|Types|Further Types|Formula
|---|---|---|---|
|Classification|Accuracy|Accuracy Score|$$\frac {T_P}{n}$$
|||Balanced Accuracy Score|$$\frac {Senstivity + Specifisity}{2}$$
|||Top K Accuracy|$$argmax[accuracy][:k]$$
||Precison|Average Precision Score|$$\frac {1}{n}\sum\limits_{i = 1}^{n}(\frac {True_-Ones}{True_-Ones + False_-Ones})$$
|||Precision Score|$$\frac {True_-Ones}{True_-Ones + False_-Ones}$$
||F-1 Score|Normal|$$\frac {1}{\frac {1}{Precision} + \frac {1}{Recall}}$$
|||Micro|$$\frac {T_P}{T_P + \frac {1}{2}(F_P + F_N)}$$
|||Macro|$$\frac {2(precision_-recall}{precision + recall}$$
|Regression|Error|Max Error|$$\sum\limits_{i = 1}^{n}(y - \hat y)$$
|||Mean Absolute Error|$$\frac {1}{n}\sum\limits_{i = 1}^{n}|y - \hat y|$$
|||Mean Squared Error|$$\frac {1}{n}\sum\limits_{i = 1}^{n}(y - \hat y)^2$$
|||Root Mean Squared Error|$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}(y - \hat y)^2}$$
|||Root Mean Squared Log Error|$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}(log(y) - log(\hat y))^2}$$
||R2|R2 Score|$$1 - \sum\limits_{i = 1}^{n}\frac{(y - \hat y)^2}{(y - \bar y)^2}$$
