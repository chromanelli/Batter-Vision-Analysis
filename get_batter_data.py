import pybaseball as pyb
import pandas as pd
import os
import batter_vision as bv
import strikezone_graphs as sz
from vision_analysis import analysis

all_vsa = []
all_vsb = []
all_vsc = []
all_apal = []
all_pa = []
all_ba = []
all_so = []

def fix_name(player_name):
    f_name = player_name[0]
    l_name = player_name[1]
    ret = f_name[0].upper() + f_name[1:] + " " + l_name[0].upper() + l_name[1:]
    return ret

def get_data(player_name, s_dt, e_dt):
    batter = pyb.playerid_lookup(player_name[1], player_name[0])
    b_id = batter['key_mlbam'].values[0]

    print("Searching: {:} ({:})".format(p_name, b_id))

    batter_data = pyb.statcast_batter(s_dt, e_dt, b_id)
    batter_data = batter_data[["game_date", "batter", "pitcher", "events", "description",
    "zone", "des", "balls", "strikes", "outs_when_up", "pitch_number", "inning", "plate_x", "plate_z"]]
    batter_data.to_csv("data/" + p_name + "/at_bats.csv")

    overall_data = pyb.batting_stats_range(s_dt, e_dt)
    overall_data = overall_data.loc[overall_data["Name"] == fix_name(player_name)]

    vsa, vsb, vsc, apal = bv.vision_score(p_name, s_dt, e_dt, overall_data)
    sz.make_strikezone_graph(p_name)

    all_vsa.append(vsa)
    all_vsb.append(vsb)
    all_vsc.append(vsc)
    all_apal.append(apal)
    all_pa.append(overall_data["PA"].values[0])
    all_ba.append(overall_data["BA"].values[0])
    all_so.append(overall_data["SO"].values[0])

    return

# player_name = input("Enter the batter's name: ").lower().split()
# p_name = player_name[0] + "_" + player_name[1]
# s_dt = input("Enter start date: ")
# e_dt = input("Enter end date: ")

# dir_path = "data/" + p_name + "/"
# if os.path.exists(dir_path) == False: os.mkdir(dir_path)

# get_data(player_name, s_dt, e_dt)

players_to_search = ["xander_bogaerts", "rafael_devers", "alex_verdugo", "trevor_story", "freddie_freeman", "mookie_betts",
"aaron_judge", "giancarlo_stanton", "ozzie_albies", "dansby_swanson", "shohei_ohtani", "mike_trout", "tony_kemp", "juan_soto",
"eric_hosmer", "francisco_lindor", "christian_yelich", "didi_gregorius", "hunter_renfroe", "kyle_schwarber", "marcus_semien",
"mitch_haniger", "bo_bichette", "cedric_mullins", "jose_altuve", "salvador_perez", "kyle_tucker", "joey_gallo", "anthony_rizzo",
"christian_arroyo", "enrique_hernandez", "yu_chang", "jonathan_schoop", "jon_berti", "byron_buxton", "trey_mancini", "lane_thomas",
"albert_pujols", "khris_davis", "taylor_jones", "nick_senzel", "richie_martin", "riley_adams", "luke_williams", "pablo_sandoval",
"mike_zunino", "gavin_lux", "starlin_castro", "elias_diaz", "matt_olson", "joey_votto", "josh_rojas", "nathaniel_lowe", "nick_solak",
"ian_happ", "myles_straw", "miguel_sano", "paul_goldschmidt", "yordan_alvarez", "wil_myers", "justin_turner", "carlos_correa",
"max_muncy", "adam_duvall", "miguel_cabrera", "ty_france", "jonathan_india", "nick_castellanos", "andrew_benintendi", "kris_bryant"]

s_dt = "2021-04-01"
e_dt = "2021-10-04"

for p_name in players_to_search:
    dir_path = "data/" + p_name + "/"
    if os.path.exists(dir_path) == False: os.mkdir(dir_path)
    player_name = p_name.split("_")
    get_data(player_name, s_dt, e_dt)
    exit()

data = {"name": players_to_search, "vsa": all_vsa, "vsb": all_vsb, "vsc": all_vsc, 
"apal": all_apal, "pa": all_pa, "ba": all_ba, "so": all_so}

vision_data = pd.DataFrame(data)
vision_data.to_csv("data/overall.csv")
analysis()
