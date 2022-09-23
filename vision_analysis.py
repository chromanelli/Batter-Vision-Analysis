import pandas as pd
import matplotlib.pyplot as plt

def analysis():
    data = pd.read_csv("data/overall.csv")
    # high = data.loc[(data["ba"] > 0.300) | (data["vsc"] > 0.450)]
    # print(high)
    
    ba_y = data["ba"].values
    vsa_x = data["vsa"].values
    vsb_x = data["vsb"].values
    vsc_x = data["vsc"].values
    apal_x = data["apal"].values

    plt.scatter(vsa_x, ba_y)
    plt.title("Vision Score Version A")
    plt.ylabel("Batting Average")
    plt.xlabel("Vision Score")
    plt.savefig("graphs/vsa_analysis.jpeg")
    plt.close()

    plt.scatter(vsb_x, ba_y)
    plt.title("Vision Score Version B")
    plt.ylabel("Batting Average")
    plt.xlabel("VSB")
    plt.savefig("graphs/vsb_analysis.jpeg")
    plt.close()

    plt.scatter(vsc_x, ba_y)
    plt.title("Vision Score Version C")
    plt.ylabel("Batting Average")
    plt.xlabel("VSC")
    plt.savefig("graphs/vsc_analysis.jpeg")
    plt.close()

    plt.scatter(apal_x, ba_y)
    plt.title("APAL")
    plt.ylabel("Batting Average")
    plt.xlabel("APAL")
    plt.savefig("graphs/apal_analysis.jpeg")
    plt.close()

    data_good_ba = data.loc[data["ba"] > 0.243]
    data_bad_ba = data.loc[data["ba"] <= 0.243]

    x_good = data_good_ba["vsa"].values
    y_good = data_good_ba["apal"].values

    x_bad = data_bad_ba["vsa"].values
    y_bad = data_bad_ba["apal"].values

    plt.scatter(x_good, y_good, color="blue", label="Above League Avg BA")
    plt.scatter(x_bad, y_bad, color="red", label="Below League Avg BA")
    plt.legend()
    plt.title("Vision Score A vs APAL")
    plt.ylabel("APAL")
    plt.xlabel("Vision Score A")
    plt.savefig("graphs/vsa_apal.jpeg")
    plt.close()

    x_good = data_good_ba["vsb"].values
    y_good = data_good_ba["apal"].values

    x_bad = data_bad_ba["vsb"].values
    y_bad = data_bad_ba["apal"].values

    plt.scatter(x_good, y_good, color="blue", label="Above League Avg BA")
    plt.scatter(x_bad, y_bad, color="red", label="Below League Avg BA")
    plt.legend()
    plt.title("Vision Score B vs APAL")
    plt.ylabel("APAL")
    plt.xlabel("Vision Score B")
    plt.savefig("graphs/vsb_apal.jpeg")
    plt.close()
    
    return
