import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

data = pd.read_csv("regression/vs_metrics.csv")
print(data)

X = data[["sw", "st", "bs", "bt"]].values
y = data["obp"].values

regr = linear_model.LinearRegression()
regr.fit(X, y)

predicted_obp = regr.predict([[890, 280, 400, 930]])
print(predicted_obp)
print(regr.coef_)
print(regr.intercept_)

all_vs = []
all_obp = []

for i in data.values:
    vs = i[5]
    for j in range(1, 5):
        vs += (regr.coef_[j-1] * i[j])
    print("{:}: {:.3f} {:.3f}".format(i[0], vs, i[6]))
    all_vs.append(vs)
    all_obp.append(i[6])

plt.scatter(all_vs, all_obp)
plt.savefig("regression/test.jpeg")
