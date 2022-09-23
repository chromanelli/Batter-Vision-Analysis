import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/overall.csv")

high_obp = data.loc[data["obp"] > 0.316]
low_obp = data.loc[data["obp"] <= 0.316]

x_good = high_obp["vsc"].values
y_good = high_obp["ba"].values

x_bad = low_obp["vsc"].values
y_bad = low_obp["ba"].values

plt.scatter(x_good, y_good, color="blue", label="Above League Avg OBP")
plt.scatter(x_bad, y_bad, color="red", label="Below League Avg OBP")
plt.legend()
plt.title("Vision Score C vs BA")
plt.ylabel("BA")
plt.xlabel("Vision Score C")
plt.savefig("graphs/vsc_obp.jpeg")
plt.close()

high_ba = data.loc[data["ba"] > 0.243]
low_ba = data.loc[data["ba"] <= 0.243]

x_good = high_ba["vsc"].values
y_good = high_ba["obp"].values

x_bad = low_ba["vsc"].values
y_bad = low_ba["obp"].values

plt.scatter(x_good, y_good, color="blue", label="Above League Avg BA")
plt.scatter(x_bad, y_bad, color="red", label="Below League Avg BA")
plt.legend()
plt.title("Vision Score C vs OBP")
plt.ylabel("OBP")
plt.xlabel("Vision Score C")
plt.savefig("graphs/vsc_ba.jpeg")
plt.close()