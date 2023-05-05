This repo is an attempt to make machine learning more grounded. Starting with basics and creating advanced level code is the motive behind this repo
|Techinques|_____________________||________________________||
|---|---|---|---|---
|Models|Decision Trees|
||Random Forest|
||Gaussian Naive Bayes|
||K Nearest Neighbors
||Lasso Regression
||Linear Regression
||Ridge Regression|
||SGD Regressor|
|Metrics|Classification|Accuracy|Accuracy Score|$$\frac {T_P + T_N}{T_P + T_N + F_P + F_N}$$
||||Balanced Accuracy Score|$$\frac {sensitivity + specifictiy}{2}$$
||||Top K Accuracy|$$argmax[accuracy][:k]$$
|||F-1 Score|Macro|$$\frac {2(precision_-recall}{precision + recall}$$
||||Micro|$$\frac {T_P}{T_P + \frac {1}{2}(F_P + F_N)}$$
||||Normal|$$\frac {1}{\frac {1}{Precision} + \frac {1}{Recall}}$$
|||Precision|Average Precision|$$\frac {1}{n}\sum\limits_{i = 1}^{n}(\frac {True_-Ones}{True_-Ones + False_-Ones})$$
||||Precision Score|$$\frac {True_-Ones}{True_-Ones + False_-Ones}$$
||Regression|Error|Max Error|$$\sum\limits_{i = 1}^{n}(y - \hat y)$$
||||Mean Squared Error|$$\frac {1}{n}\sum\limits_{i = 1}^{n}(y - \hat y)^2$$
||||Mean Absolute Error|$$\frac {1}{n}\sum\limits_{i = 1}^{n}|y - \hat y|$$
||||Root Mean Squared Error|$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}(y - \hat y)^2}$$
||||Root Mean Squared Log Error|$$\sqrt{\frac {1}{n}\sum\limits_{i = 1}^{n}(log(y) - log(\hat y))^2}$$
|||R Score|R2 Score|$$1 - \sum\limits_{i = 1}^{n}\frac{(y - \hat y)^2}{(y - \bar y)^2}$$
|Encoding Techniques|One Hot Encoder
||Ordinal Encoder
|Cross Validation
|Function Transformmers|Log Transformer|$$y = log(x)$$
||Box-Cox Transformer|
||Square Transformer| $$y = x^2$$
||Yeo Johnson Transformer
|Mutual Information|
|Principal Component Analysis
|Scaling|Min Max Scaler|$$x_{sclaed} = \frac {x_{i} - x_{min}}{x_{max} - x_{min}}$$
||Standard Scaler|$$x_{scaled} = \frac {x_{i} - x_{mean}}{\sigma}$$
