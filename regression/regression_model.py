import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

data = pd.read_csv("regression/vs_metrics.csv")

X = data[["sw", "st", "bs", "bt", "ba"]].values
y = data["obp"].values

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
print(regr.intercept_)
preds = regr.predict(X)
print(r2_score(y, preds))

plt.scatter(preds, y)
# plt.plot(y, preds, color="red")
plt.xlabel("Regression Vision Score")
plt.ylabel("OBP")
plt.title("Regression Score vs OBP")
plt.savefig("regression/regression_results.jpeg")
plt.close()
