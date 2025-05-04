from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Me\Desktop\SupervisedLearning\student_exam.csv')

print(df.isnull().sum())

cols = ['Hours_Studied','Attendance','Assignments_Completed','Passed_Exam']

for col in cols:
    df[col] = df[col].fillna(df[col].mean())
    
features = ['Hours_Studied','Attendance','Assignments_Completed']
target = 'Passed_Exam'

X = df[features]
Y = df[target]

loo = LeaveOneOut()
loo_scores =[]

model = LogisticRegression()

for train_index,test_index in loo.split(X):
    X_train,X_test = X.iloc[train_index],X.iloc[test_index]
    Y_train,Y_test = Y.iloc[train_index],Y.iloc[test_index]
    
    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test,y_pred)
    loo_scores.append(acc)

print("LOOCV Average Accuracy:", np.mean(loo_scores))