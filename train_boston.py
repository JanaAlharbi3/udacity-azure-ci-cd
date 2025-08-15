import os, pandas as pd, joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
FEATURES = ["CHAS","RM","TAX","PTRATIO","B","LSTAT"]

url = "https://raw.githubusercontent.com/noahgift/boston_housing_pickle/master/housing.csv"
names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
df = pd.read_csv(url, delim_whitespace=True, names=names)
X = df[FEATURES]
y = df["MEDV"]

pipe = Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())])
pipe.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(pipe, "model/model.joblib")
print("Saved model to model/model.joblib")
