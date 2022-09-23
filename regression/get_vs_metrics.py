import pandas as pd

def save_vs_data(name, sw, st, bs, bt, ba, obp):
    data = {"name": name, "sw": sw, "st": st, "bs": bs, "bt": bt, "ba": ba, "obp": obp}
    df = pd.DataFrame(data)
    df.to_csv("regression/vs_metrics.csv", mode='a', index=False, header=False)
    return
