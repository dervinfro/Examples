import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
df = pd.read_csv('/Users/user/Downloads/Python Airdroped 13MAY2020/diabetes.csv', header=None, names=col_names)

pd.options.display.max_columns=None
pd.options.display.width = 150

'''
This is in ref to a logistic regression tutorial.
 - https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

The datasource comes from kaggle.
 - https://www.kaggle.com/uciml/pima-indians-diabetes-database?select=diabetes.csv

'''

print(df.sample(10))

feature_cols = ['pregnant','insulin','bmi','age','glucose','bp','pedigree']
X = df[feature_cols] # features
y = df.label # Target variable

#SPLIT X AND Y INTO TRAINING AND TEST SETS
#the dataset is being broken into two parts with a ratio of 75% and 25%.  75% for training and 25% for testing.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=0) 

#instantiate the model using the default parameters
log_reg = LogisticRegression(max_iter=10000)

# fit the model with the data
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)


# MODEL EVALUATION USING THE CONFUSION MATRIX
conf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(conf_matrix)

'''
Output from above:
[[118  12]
 [ 26  36]]

For the full read-out on confusion matrix see:
https://medium.com/analytics-vidhya/what-is-a-confusion-matrix-d1c0f8feda5
 
 - the columns are Actual Values
 - the rows are Predicted Values
 
 118 = The predicted value is negative and it is negative. (AKA: True Negative (TN))
 26 = Type II error: The predicted value is negative but it is Positive. (AKA: False Negative (FN))
 12 = Type I error: The predicted value is positive but it is False. (AKA: False Positive (FP))
 36 = The predicted value is positive (AKA: True Positive (TP))
'''

print('Classification Report: ', classification_report(y_test, y_pred), sep='\n')

#graph out the confusion matrix
class_names=[0,1]
fig, axes = plt.subplots(2,1,figsize=(8,8)) #subplot with 1 row and 2 graphs in that 1 row.

#setting the sns.heatmap as the first, of two, graphs on the subplot
sns.heatmap(pd.DataFrame(conf_matrix), annot=True, cmap='YlGnBu', fmt='g', ax=axes[0])
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
axes[0].set_title('Confusion Matrix')
axes[0].set_ylabel('Actual Label')
axes[0].set_xlabel('Predicted Label')

#setting the logistic regression (sigmoid activation funtion) as the second, of two, graphs on the subplot
'''
GRAPH NOT BUILT - AS OF: 7JAN 2021
'''
plt.show()

#Evalution Metrics
#Accuracy - measures how often the classifier makes the correct prediction.
print('Accuracy: ', metrics.accuracy_score(y_test, y_pred)) # the number of values correctly predicted (TP + TN / (TP + FP + TN + FN))

#Precision - a metric in cases where False Positive is a higher concern than False Negatives”
print('Precision: ', metrics.precision_score(y_test, y_pred)) # total number of correct positive classes OVER total number of predictive positive classes (TP / (TP+FP)).  Should be close to 1

#Recall - a metric in cases where False Negative trumps False Positive
print('Recall: ', metrics.recall_score(y_test, y_pred)) # ratio of the total number of correctly classified positive classes divide by the total number of positive classes( TP / (TP + FN)).  Should be close to 1.





