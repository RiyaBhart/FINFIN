import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv(r'C:\Users\Me\Desktop\lab9\emails.csv')
df = df.fillna(' ')

vectorizer = TfidfVectorizer(stop_words='english',max_features=3000)
X= vectorizer.fit_transform(df['text'])
Y = df['label']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = SVC()
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,y_pred)

print("accuracy : ",accuracy)

new_email = ["hi this is riya, can i talk to you?"]
new_email_transformed = vectorizer.transform(new_email)
prediction = model.predict(new_email_transformed)

print("prediction : ","spam" if prediction[0]==1 else "not spam")