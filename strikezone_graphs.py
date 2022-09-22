import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def make_strikezone_graph(player_name):
    swing_calls = ["swinging_strike", "foul", "hit_into_play"]
    df = pd.read_csv("data/" + player_name + "/at_bats.csv")

    swings = df.loc[df["description"].isin(swing_calls)]
    takes = df.loc[~df["description"].isin(swing_calls)]

    s_x = swings["plate_x"].values
    s_y = swings["plate_z"].values

    t_x = takes["plate_x"].values
    t_y = takes["plate_z"].values

    plt.figure(figsize=(8.0, 6.5))
    plt.xlim([-3.5, 3.5])
    plt.ylim([-1.0, 6.0])
    plt.scatter(s_x, s_y, color="red", label="Swings")
    plt.scatter(t_x, t_y, color="blue", label="Takes")
    plt.legend()
    plt.axvline(x=-0.71, color="black")
    plt.axvline(x=0.71, color="black")
    plt.axhline(y=1.5, color="black")
    plt.axhline(y=3.5, color="black")
    plt.title(player_name + " zone report")
    plt.savefig("data/" + player_name + "/zone_report.jpeg")
    plt.close()

    return