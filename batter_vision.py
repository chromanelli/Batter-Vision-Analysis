import pandas as pd
import pybaseball as pyb
from regression.get_vs_metrics import save_vs_data

swings = ["swinging_strike", "foul", "hit_into_play"]
end_events = ["strikeout", "walk", "field_error", "field_out", "single",
    "double", "triple", "home_run", "grounded_into_double_play", "double_play",
    "force_out", "hit_by_pitch", "sac_fly", "fielders_choice"]

def vision_score(player_name, s_dt, e_dt, overall_data, verbose):
    batter_data = pd.read_csv("data/" + player_name + "/at_bats.csv")
    
    strike_swing = 0
    strike_take = 0
    ball_swing = 0
    ball_take = 0

    total_strikes = 0
    total_balls = 0
    total_so = overall_data["SO"].values[0]
    total_bb = overall_data["BB"].values[0]

    ab_length = 0

    for index, row in batter_data.iterrows():
        if row["zone"] <= 9:
            if row["description"] in swings:
                strike_swing += 1
            else:
                strike_take += 1
            total_strikes += 1
        else:
            if row["description"] in swings:
                ball_swing += 1
            else: ball_take += 1
            total_balls += 1
        if row["events"] in end_events:
            ab_length += int(row["pitch_number"])

    v_score_a = ((strike_swing + ball_take) - (strike_take + ball_swing)) / len(batter_data)

    apal = ab_length
    total_pa = overall_data["PA"].values[0]
    
    so_rate = overall_data["SO"].values[0]/total_pa
    v_score_b = v_score_a - so_rate
    
    bb_rate = overall_data["BB"].values[0]/total_pa
    v_score_c = v_score_b + bb_rate

    with open("data/" + player_name + "/at_bats.txt", 'w') as f:
        f.write("\nVISION REPORT: {:} ({:} thru {:})\n".format(player_name, s_dt, e_dt))
        f.write("     Total PA: {:}\n".format(total_pa))
        f.write("     Strikes Swung At: {:} ({:.2f}%)\n".format(strike_swing, 100 * strike_swing/total_strikes))
        f.write("     Strikes Taken: {:} ({:.2f}%)\n".format(strike_take, 100 * strike_take/total_strikes))
        f.write("     Balls Swung At: {:} ({:.2f}%)\n".format(ball_swing, 100 * ball_swing/total_balls))
        f.write("     Balls Taken: {:} ({:.2f}%)\n".format(ball_take, 100 * ball_take/total_balls))
        f.write("     Strikeouts: {:}\n".format(total_so))
        f.write("     Walks: {:}\n".format(total_bb))
        f.write("     {:} saw {:} strikes and {:} balls\n\n".format(player_name, total_strikes, total_balls))
        f.write("VISION SCORE METRIC A (SSA+BT)/(ST+BSA): {:.4f}\n".format(v_score_a))
        f.write("VISION SCORE METRIC B (VSA - SO%): {:.4f}\n".format(v_score_b))
        f.write("VISION SCORE METRIC C (VSB + BB%): {:.4f}\n\n".format(v_score_c))
        f.write("Average PA Length: {:.4f} ({:}/{:})\n".format(apal/total_pa, apal, total_pa))
        f.write("Batting Avg: {:.3f}\n".format(overall_data["BA"].values[0]))
        f.write("OBP: {:.3f}\n".format(overall_data["OBP"].values[0]))
    f.close()

    if verbose == True:
        print("\nVISION REPORT: {:} ({:} thru {:})".format(player_name, s_dt, e_dt))
        print("     Total PA: {:}".format(total_pa))
        print("     Strikes Swung At: {:} ({:.2f}%)".format(strike_swing, 100 * strike_swing/total_strikes))
        print("     Strikes Taken: {:} ({:.2f}%)".format(strike_take, 100 * strike_take/total_strikes))
        print("     Balls Swung At: {:} ({:.2f}%)".format(ball_swing, 100 * ball_swing/total_balls))
        print("     Balls Taken: {:} ({:.2f}%)".format(ball_take, 100 * ball_take/total_balls))
        print("     Strikeouts: {:}".format(total_so))
        print("     Walks: {:}".format(total_bb))
        print("     {:} saw {:} strikes and {:} balls\n".format(player_name, total_strikes, total_balls))
        print("VISION SCORE METRIC A (SSA+BT)/(ST+BSA): {:.4f}".format(v_score_a))
        print("VISION SCORE METRIC B (VSA - SO%): {:.4f}".format(v_score_b))
        print("VISION SCORE METRIC C (VSB + BB%): {:.4f}\n".format(v_score_c))
        print("Average PA Length: {:.4f} ({:}/{:})".format(apal/total_pa, apal, total_pa))
        print("Batting Avg: {:.3f}".format(overall_data["BA"].values[0]))
        print("OBP: {:.3f}\n".format(overall_data["OBP"].values[0]))
    
    # save_vs_data([player_name], [strike_swing], [strike_take], [ball_swing], [ball_take], overall_data["BA"], overall_data["OBP"])

    return v_score_a, v_score_b, v_score_c, apal/total_pa
