# Metrics
Metrics in machine learning refer to the quantitative measurements used to evaluate the performance of a model. Metrics can be used to assess different aspects of a model's performance, such as accuracy, precision, recall, F1-score, AUC-ROC, and others. Choosing the right metrics for a given problem is important to ensure that the model's performance is appropriately evaluated and improved.

<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6F58yqU8uacM3fV56Thy1CGgc-qRTBWocOA&usqp=CAU">

|Classification|Further Types|Formula
|---|---|---|
|Accuracy|Accuracy Score|$$\frac {T_P}{n}$$
||Balanced Accuracy Score|$$\frac {Senstivity + Specifisity}{2}$$
||Top K Accuracy|$$argmax[accuracy][:k]$$
|Precison|Average Precision Score|$$\frac {T_P}{F_N}$$
|F-1 Score|Normal|$$\frac {1}{\frac {1}{Precision} + \frac {1}{Recall}}$$
||Micro|$$\frac {T_P}{T_P + \frac {1}{2}(F_P + F_N)}$$
||Macro|$$\frac {2(precision_-recall}{precision + recall}$$
