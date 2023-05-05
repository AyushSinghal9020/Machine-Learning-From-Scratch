# Mutual Info 

Mutual information (MI) is a statistical measure commonly used in machine learning and information theory to quantify the degree of dependency or correlation between two random variables. Specifically, MI measures the amount of information that one variable provides about the other variable.

In the context of machine learning, MI can be used for feature selection, where it helps to identify which features are most informative for a given task. For example, in a classification problem, features with high MI values are likely to be more useful for distinguishing between different classes.

MI values range from 0 to a maximum value that depends on the range and distribution of the variables. A higher MI value indicates a stronger dependency between the variables.

MI is a useful tool in machine learning because it is model-agnostic, meaning it can be used with any type of model or data. However, it may not capture all types of dependencies between variables, such as nonlinear relationships or interactions between multiple variables.

****
$$$$= \sum\limits_{x = 1}^{n}\sum\limits_{y = 1}^{n}.{P}(x , y)log\Bigg[\frac{{P}(x , y)}{_P(x)_P{y}}\Bigg]$$
****

**Note** 
* This notebook is higly inspired from the [Youtube Video](https://www.youtube.com/watch?v=eJIp_mgVLwE), kudos to the person for being a great teacher
* Pandas was only used to view the dataframe in a convinient way
