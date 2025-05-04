from sklearn.model_selection import KFold
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

kf = KFold(n_splits=5, shuffle = True, random_state=42)
model = LogisticRegression()

accuracy_scores=[]

for train_index,test_index in kf.split(X):
    X_train,X_test = X.iloc[train_index],X.iloc[test_index]
    Y_train,Y_test = Y.iloc[train_index],Y.iloc[test_index]
    
    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test,y_pred)
    accuracy_scores.append(acc)

print("K-Fold CV Average Accuracy: ",np.mean(accuracy_scores))

from sklearn.tree import DecisionTreeClassifier 
# Initialize the DecisionTreeClassifier 
DT = DecisionTreeClassifier() 
 
# Train the model 
ModelDT = DT.fit(X_train, Y_train) 
 
# Model Testing (Prediction) 
PredictionDT = DT.predict(X_test) 
print("Predictions:", PredictionDT) 
 
# Model Training Accuracy 
print('====================DT Training Accuracy===============') 
tracDT = DT.score(X_train, Y_train)  
TrainingAccDT = tracDT * 100 
print(f"Training Accuracy: {TrainingAccDT:.2f}%") 
 
# Model Testing Accuracy 
print('=====================DT Testing Accuracy=================') 
teacDT = accuracy_score(Y_test, PredictionDT) 
testingAccDT = teacDT * 100 
print(f"Testing Accuracy: {testingAccDT:.2f}%")