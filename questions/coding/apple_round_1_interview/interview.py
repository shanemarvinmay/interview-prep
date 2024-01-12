'''
responses
[{
got:True
expected:False
}]
'''
def metrics(responses):
    return (precision(responses), recall(responses))

def precision(responses):
    '''TP/ (TP + FP)'''
    tp, fp = 0, 0
    for response in responses:
        if response['got'] == False:
            continue
        if response['expected']:
            tp += 1
        else:
            fp += 1
    
    if tp == 0 and fp == 0:
        return 0
    return tp / (tp + fp)

def recall(responses):
    '''TP/ (TP + FN)'''
    pass
