import pandas as pd
import numpy as np

max_centers = 2
max_left_wings = 2
max_right_wings = 2
max_defensemen = 4
max_goalies = 2
days = {
    'M': 'Monday',
    'T': 'Tuesday',
    'W': 'Wednesday',
    'R': 'Thursday',
    'F': 'Friday',
    'S': 'Saturday',
    'U': 'Sunday'
}

def build_team(sorted_arr, day):
    cs = lws = rws = ds = gs = np.empty(1)
    for player in sorted_arr:
        if day in player[6]:
            if 'C' in player[2:4] and len(cs) <= max_centers:
                cs = np.append(cs, player[0])
            elif 'LW' in player[2:4] and len(lws) <= max_left_wings:
                lws = np.append(lws, player[0])
            elif 'RW' in player[2:4] and len(rws) <= max_right_wings:
                rws = np.append(rws, player[0])
            elif 'D' in player[2:4] and len(ds) <= max_defensemen:
                ds = np.append(ds, player[0])
            elif 'G' in player[2:4] and len(gs) <= max_goalies:
                gs = np.append(gs, player[0])

    print("Roster for", days[day]+":")
    print("Centers:", cs)
    print("Left Wings", lws)
    print("Right Wings", rws)
    print("Defensemen", ds)
    print("Goalies", gs, end="\n\n")


players_data = pd.read_csv('players.csv')
players_array = np.array(players_data.to_numpy())
sorted_arr = players_array[players_array[:, 5].argsort()] #sorts players array by priority

build_team(sorted_arr, 'M')
build_team(sorted_arr, 'T')
build_team(sorted_arr, 'W')
build_team(sorted_arr, 'R')
build_team(sorted_arr, 'F')
build_team(sorted_arr, 'S')
build_team(sorted_arr, 'U')

input('Press ENTER to exit')