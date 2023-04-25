|Metrics|Further Types|Formula
|---|---|---|
|Accuracy|Accuracy Score|$$\frac {T_P}{n}$$
||Balanced Accuracy Score|$$\frac {Senstivity + Specifisity}{2}$$
||Top K Accuracy|$$argmax[accuracy][:k]$$
|Precison|Average Precision Score|$$\frac {1}{n}\sum\limits_{i = 1}^{n}(\frac {True_-Ones}{True_-Ones + False_-Ones})$$
||Precision Score|$$\frac {True_-Ones}{True_-Ones + False_-Ones}$$
|F-1 Score|Normal|$$\frac {1}{\frac {1}{Precision} + \frac {1}{Recall}}$$
||Micro|$$\frac {T_P}{T_P + \frac {1}{2}(F_P + F_N)}$$
||Macro|$$\frac {2(precision_-recall}{precision + recall}$$
