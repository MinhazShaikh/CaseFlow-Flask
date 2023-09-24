import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data=pd.read_csv('newdatacase.csv')
data.dtypes
X = data.drop(columns=[ "Case Type","Case Type.1","Filing Date","Charges","IPC Section","Case Number","Priority"])  # Features
y = data["Priority"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
print(X)
model = RandomForestClassifier(random_state=42)
print(X_train)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

pickle.dump(model,open('save','wb'))
model_loaded=pickle.load(open('save','rb'))