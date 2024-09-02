# fantasy-hockey-team-builder
 Script which helps you build fantasy hockey teams for any given week.

# Usage
1. Download latest build
2. Run the exe
3. Enter path of csv file used.
4. Let the script run, will show you the players iced for each day of the week and how many slots are available with the given roster.

# Editing the CSV File
There are a few things to keep in mind when editing and creating CSV files for this script. A sample CSV has been provided.
1. There are 6 columns in the following order:
    - Name
    - Pos1
    - Pos2
    - Pos3
    - Priority
    - Days
2. Each position must be entered as the abbreviated form of that position, valid entries would be:
    - C
    - LW
    - RW
    - D
    - G
3. Priority indicates the preference the script will give to that player. A lower number will indicate higher priority. The higher priority players will be preferred over lower priority players when selecting who to ice.
4. For the days column, each day of the week corresponds to a letter. The letters used are:
    - M for Monday
    - T for Tuesday
    - W for Wednesday
    - R for Thursday
    - F for Friday
    - S for Saturday
    - U for Sunday
   A letter for each day of the week that player is playing should be entered into the program. For example, if a player is playing on wednesday, saturday, and sunday, you would put WSU in the days column for that player.