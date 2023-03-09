def f1_score_micro(pred , act):
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

    f1_score_1 = tp / (tp + ((1/2) * (fp + fn)))
    f1_score_0 = tn / (tn + ((1/2) * (fp + fn)))

    return f1_score_1 , f1_score_0
