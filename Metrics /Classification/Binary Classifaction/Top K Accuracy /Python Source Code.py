def top_k_accuracy(pred , act):
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

    tp , tn , fp , fn = metric_values(pred , act)

    precision_0 = tp / (tp + tn)
    precision_1 = fp / (fp + fn)

    precision_list = [precision_0 + precision_1]

    return max(precision_list)
