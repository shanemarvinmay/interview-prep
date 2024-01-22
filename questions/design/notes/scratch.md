# Technologies and Terms to Look up:
kafka ("event bus")
- handles events

http poling (- latency)

web sockets 

sharding database 
- shard id (primary key)

webhook

redis db

spark

Topic:
- redundancy (for failure)


-------------

gradient descent

bias / variance trade off
- bias: how far off the model typicaly is
- variance: how big the spread of model output is
- model complexity (num of basis functions) effects the balance between bias and variance
    - more complexity means more variance and less bias
        - ? overfitting ?
    - simplier model means more bias and less variance
        - ? underfitting ?
- find a balance for the best model is most cases

no labels, what do you do
- supervised learning
- vialize data to gain insight

confusion matrix (error matrix)
- tp, fn
- f1 scores (f measure, f score)
    - ```2 * (precision * recall) / (precision + recall) ```
    - balance between precision and recall
    - good for imbalanced datasets
- accuracy: how correct is the model overall
    - useful when classes are blanced, but maybe not if you want your model to predict something that isn't balanced. like spam, 90% emails are not spam, so the real world data isn't balanced.
        - so if the model just always said the email wasn't spam, the accuracy would look GREAT! but it could also be just saying everything isn't spam and still getting the 90%
    - ``` correct predictions / all predictions ```
    - ``` (TP + TN) / (TP + TN + FP + FN)```
- precision: how good the model is at predicting a class. This class can be a bool and could be how many of the yes's are true
    - good at looking how one class is predicted
    - good for unbalanced datasets
    - useful when the cost of FP is high
        - you want to be more precision, even if you miss a few
    - Doesn't account for FN, so we don't know how much we are missing out on
    - ``` TP / (TP + FP)```
- recall
    - ``` TP / (TP + FN)```
    - useful with unbalanced datasets
    - uesful with the cost of missing TP (or getting a FN) is high
    - downside, you don't account for FP. So saying YES everytime will give you 100% recall but everything else will be terrible


outliers and anoymolies
- outlier is uncommon but still part of the bell curve of your data. Uncommon, but still expected sometimes
- anomoly: you would really never expected it

? knn ?
- supervised classifier that isn't a parametric line
- uses proximity to make predictions (clusters)

grid search
- how to find hperparameters

Behavorial

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

meeting vs work

stack: what tools are being used for the project

bringing in model I build
- or new idea
- who do I give it too

any big technical challenges the team is faceing
- i know this project is needing to be migrated, but besides that

mobility apple

worst part of apple
- What is something you wish were different about your job?

What is unique about working at this company that you have not experienced elsewhere?

most important attribute of an ideal canidate

what does ramp up look like on the team

What are the strengths and weaknesses of the current team? What is being done to improve upon the weaknesses?

```````````````````````````````````````````````````````````
decision tree is easier to understand over nueral network

pep8 python style guide