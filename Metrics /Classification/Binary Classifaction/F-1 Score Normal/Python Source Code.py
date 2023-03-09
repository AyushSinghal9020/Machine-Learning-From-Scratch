def f1_score_normal(pred . act):
    def metric_values(predicition , actual):
    
        true_negative = 0
        false_negative = 0
        false_positive = 0
        true_positive = 0

        for predictions , actuals in zip(pred , act):

            if predictions == np.unique(pred)[0]:

                if actuals == np.unique(pred)[0]:

                    true_negative += 1

                else :

                    false_negative += 1

            else :

                if actuals == np.unique(pred)[0] : 

                    false_positive += 1

                else :

                    true_positive += 1

        return true_positive , true_negative , false_positive , false_negative

    precision_1 = tp / (tp + fp)
    precision_0 = tn / (tn + fn)
    
    recall_1 = tp / (tp + fn)
    recall_0 = fp / (fp + tn) 
    
    f1_score_1 = 2 / ((1 / precision_1) + (1 / recall_1))
    f1_score_0 = 2 / ((1 / precision_0) + (1 / recall_0))

    return f1_score_1 , f1_score_0
