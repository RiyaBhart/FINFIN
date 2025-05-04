import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load data
df = pd.read_csv(r'C:\Users\Me\Desktop\lab9\house_data.csv')

print(df.isnull().sum())  
numeric_cols = ['square_footage', 'bedrooms', 'bathrooms', 'age', 'price']
nonnum_cols = ['neighborhood']

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

for col in nonnum_cols:
    df[col] = df[col].fillna(df[col].mode()[0])  

LE = LabelEncoder()
df['neighborhood_encoded'] = LE.fit_transform(df['neighborhood'])

features = ['square_footage', 'bedrooms', 'bathrooms', 'age', 'neighborhood_encoded']
target = 'price'


X = df[features]
Y = df[target]

print("\nMissing values in training features:\n", X.isnull().sum())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(Y_test, y_pred)
mse = mean_squared_error(Y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, y_pred)

print(f"\nMAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")

new_data = pd.DataFrame([{
    'square_footage': 2000,
    'bedrooms': 3,
    'bathrooms': 2,
    'age': 5,
    'neighborhood_encoded': LE.transform(['Downtown'])[0]
}], columns=features)

predicted_price = model.predict(new_data)[0]
print("\nPredicted price is", predicted_price)
