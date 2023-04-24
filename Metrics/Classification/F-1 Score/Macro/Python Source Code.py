def f1_score(actuals , predicitions):
    
    def balanced_accuracy_score(predictions , actuals):

        metrics = np.empty(shape = (2 , len(np.unique(pred)) + 1))

        for uniques in range(len(np.unique(pred))):

            x = np.empty(shape = (3))

            trues = 0
            falses = 0

            for actu , predi in zip(act , pred):

                if ((actu == np.unique(pred)[uniques]) and (predi == np.unique(pred)[uniques])):

                    trues += 1

                else :

                    falses += 1

            x[0] = uniques
            x[1] = trues
            x[2] = falses

            metrics[i] = x

        recall = []

        if metrics.shape[0] == 2:

            recall.append(metrics[0][1] / (metrics[0][1] + metrics[1][2]))
            recall.append(metrics[1][1] / (metrics[1][1] + metrics[0][2]))

        else :

            for labels in range(len(metrics)): 

                x = [j[2] 
                     for j in metrics[:labels]+metrics[labels+1:]]

                recall.append(metrics[labels][1] / (metrics[labels][1] + np.sum(np.array(x))))

        return np.sum(np.array(recall))
    
    def precision(actuals , predictions):

        k_labels = []

        for label in np.unique(pred):

            correct_ones = 0

            for actual  , predicted in zip(actuals , predictions):

                if predicted == label and actual == label:

                    correct_ones += 1

            asc = correct_ones / len(predictions)

            k_labels.append(asc)

        k_labels = np.array(k_labels)

        return k_labels
    # Changed the formula here 
    f1_score_mirco = (2 * (precision(actuals , predictions) * recall(actuals , predicitons))) / (precision(actuals , predictions) + recall(actuals , predictions))
    
    return f1_score_micro
