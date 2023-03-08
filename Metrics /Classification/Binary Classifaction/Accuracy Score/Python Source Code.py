import numpy as np

def asc(actual , predictions):
    true = 0
    false = 0
    for actuals  , predicted in zip(actual , predictions):
        if predicted == actuals:
            ture += 1
        else :
            false += 1

    asc = true / (true + false)

    return asc
