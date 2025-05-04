import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r'C:\Users\Me\Desktop\lab9\customer_data.csv')

df.dropna(inplace=True)

features = ['total_spending','age','num_visits','purchase_frequency']
target = 'customer_value'

X = df[features]
Y = df[target]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)

X_train,X_test,Y_train,Y_test = train_test_split(x_scaled,Y,test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,y_pred)
print("Accuracy is : ",accuracy)

new_customer = [[4000, 35, 12, 0.7]]
new_customer_scaled = scaler.fit_transform(new_customer)
new_pred = model.predict(new_customer_scaled)
print("prediction: ","highvalued"if new_pred==1 else "lowvalued")