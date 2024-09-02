import pandas as pd
import numpy as np

max_pos = {
    'C': 2,
    'LW': 2,
    'RW': 2,
    'D': 4,
    'G': 2
}
slots_free = {
    'C': 0,
    'LW': 0,
    'RW': 0,
    'D': 0,
    'G': 0
}
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
    cs = lws = rws = ds = gs = np.empty(0)
    for player in sorted_arr:
        if day in player[5]:
            if 'C' in player[1:3] and len(cs) <= max_pos['C']:
                cs = np.append(cs, player[0])
            elif 'LW' in player[1:3] and len(lws) <= max_pos['LW']:
                lws = np.append(lws, player[0])
            elif 'RW' in player[1:3] and len(rws) <= max_pos['RW']:
                rws = np.append(rws, player[0])
            elif 'D' in player[1:3] and len(ds) <= max_pos['D']:
                ds = np.append(ds, player[0])
            elif 'G' in player[1:3] and len(gs) <= max_pos['G']:
                gs = np.append(gs, player[0])

    slots_free['C'] += max_pos['C']-len(cs)
    slots_free['LW'] += max_pos['LW']-len(lws)
    slots_free['RW'] += max_pos['RW']-len(rws)
    slots_free['D'] += max_pos['D']-len(ds)
    slots_free['G'] += max_pos['G']-len(gs)

    print("Roster for", days[day]+":")
    print("Centers:", cs)
    print("Left Wings", lws)
    print("Right Wings", rws)
    print("Defensemen", ds)
    print("Goalies", gs, end="\n\n")

csv = input("Enter the name of the csv file: ")
try:
    players_data = pd.read_csv(csv)
except:
    print("Error reading file. Please check the name of the file, reopen the program and try again.")
    input('Press ENTER to exit')
    exit()

players_array = np.array(players_data.to_numpy())
sorted_arr = players_array[players_array[:, 4].argsort()] #sorts players array by priority

build_team(sorted_arr, 'M')
build_team(sorted_arr, 'T')
build_team(sorted_arr, 'W')
build_team(sorted_arr, 'R')
build_team(sorted_arr, 'F')
build_team(sorted_arr, 'S')
build_team(sorted_arr, 'U')
print("Slots free:", slots_free)

input('Press ENTER to exit')