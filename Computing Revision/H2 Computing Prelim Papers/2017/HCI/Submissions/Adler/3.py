##def CreateUpdateFile():
##    file_handle = open("RESULTS.txt")
##    team1, goal1, team2, goal2 = file_handle.readline().strip().split(" ")
##    file_handle.close()
##    match_results = get_match_results(goal1, goal2)
##    try:
##        file_handle = open("NEWFILE.txt", "a")
##    except FileNotFoundError:
##        file_handle = open("NEWFILE.txt", "w")
##    file_handle.write(",".join([team1, match_results[0], goal1, goal2])\
##                      + "\n")
##    file_handle.write(",".join([team2, match_results[1], goal2, goal1])\
##                      + "\n")
##    file_handle.close()

def get_match_results(goal1, goal2):
    goal1 = int(goal1)
    goal2 = int(goal2)
    if goal1 == goal2:
        return "D", "D"
    elif goal1 > goal2:
        return "W", "L"
    return "L", "W"

def CreateUpdateFile():
    #resetting the update file
    file_handle = open("NEWFILE.txt", "w")
    file_handle.close()
    
    file_handle1 = open("RESULTS.txt")
    for line in file_handle1:
        team1, goal1, team2, goal2 = line.strip().split(" ")
        match_results = get_match_results(goal1, goal2)
        try:
            file_handle2 = open("NEWFILE.txt", "a")
        except FileNotFoundError:
            file_handle2 = open("NEWFILE.txt", "w")
        file_handle2.write(",".join([team1, match_results[0], goal1, goal2])\
                          + "\n")
        file_handle2.write(",".join([team2, match_results[1], goal2, goal1])\
                          + "\n")
        file_handle2.close()
    file_handle1.close()

def ComputeTeamStat(team_name):
    file_data = get_file_data()
    team_results = [0, 0, 0, 0, 0, 0]
    #team_results = [played, wins, draws, losses, goals_for, goals_against]
    for match in file_data:
        if team_name in match:
            team1, goal1, team2, goal2 = match
            match_results = get_match_results(goal1, goal2)
            if team_name == team1:
                match_results = match_results[0]
                goals_for, goals_against = int(goal1), int(goal2)
            else: #team_name = team2
                match_results = match_results[1]
                goals_for, goals_against = int(goal2), int(goal1)
            team_results[0] += 1
            if match_results == 'W':
                team_results[1] += 1
            elif match_results == 'D':
                team_results[2] += 1
            else: #match_result = 'L'
                team_results[3] += 1
            team_results[4] += goals_for
            team_results[5] += goals_against
    #goal_difference
    team_results.append(team_results[-2] - team_results[-1])
    #points
    team_results.append(team_results[1] * 3 + team_results[2])
    
    print_header()
    played, wins, draws, losses, goals_for, goals_against, \
            goal_difference, points = team_results
    print("{0:<12}{1:^8}{2:^8}{3:^8}{4:^8}{5:^8}{6:^8}{7:^8}{8:^8}"\
          .format(team_name, played, wins, draws, losses, goals_for, \
                  goals_against, goal_difference, points))
    
def get_file_data():
    file_handle = open("RESULTS.txt")
    results = [x.split(" ") for x in file_handle.read().strip().split("\n")]
    file_handle.close()
    return results

def print_header():
    print("{0:<12}{1:^8}{2:^8}{3:^8}{4:^8}{5:^8}{6:^8}{7:^8}{8:^8}"\
          .format("Team", "P", "W", "D", "L", "GF", "GA", "GD", "Points"))
    print("=" * 76)


def quick_sort(array, index): #descending order
    if len(array) < 2:
        return array
    left = []
    right = []
    pivot = array[0]
    for i in range(1, len(array)):
        if array[i][index] > pivot[index]:
            left.append(array[i])
        else:
            right.append(array[i])
    return quick_sort(left, index) + [pivot] + quick_sort(right, index)

def GenerateTable():
    file_handle = open("TEAMS.txt")
    teams = file_handle.read().strip().split("\n")
    file_handle.close()
    file_data = get_file_data()
    results = []
    for team in teams:
        results.append(get_team_results(file_data, team))

    results = quick_sort(results, -2)
    results = quick_sort(results, -1)

    print_header()
    for team_results in results:
        team_name, played, wins, draws, losses, goals_for, goals_against,\
                   goal_difference, points = team_results
        print("{0:<12}{1:^8}{2:^8}{3:^8}{4:^8}{5:^8}{6:^8}{7:^8}{8:^8}"\
              .format(team_name, played, wins, draws, losses, goals_for, \
                      goals_against, goal_difference, points))
    

def get_team_results(file_data, team_name):
    #essentially ComputeTeamStat() but returning \
    #the results instead of printing them

    #also takes in file_data so that it does not need to be
    #created every time this function runs
    
    team_results = [0, 0, 0, 0, 0, 0]
    #team_results = [played, wins, draws, losses, goals_for, goals_against]
    for match in file_data:
        if team_name in match:
            team1, goal1, team2, goal2 = match
            match_results = get_match_results(goal1, goal2)
            if team_name == team1:
                match_results = match_results[0]
                goals_for, goals_against = int(goal1), int(goal2)
            else: #team_name = team2
                match_results = match_results[1]
                goals_for, goals_against = int(goal2), int(goal1)
            team_results[0] += 1
            if match_results == 'W':
                team_results[1] += 1
            elif match_results == 'D':
                team_results[2] += 1
            else: #match_result = 'L'
                team_results[3] += 1
            team_results[4] += goals_for
            team_results[5] += goals_against
    #goal_difference
    team_results.append(team_results[-2] - team_results[-1])
    #points
    team_results.append(team_results[1] * 3 + team_results[2])

    return [team_name] + team_results
