from ..structure.foundation import Tournament

def getWinnerProbabilities(tournament, numSimulations=100000):
    
    teamNames = getTeamNames(tournament)
    winCounts = initializeWinCounts(teamNames)
    
    for i in range(numSimulations):
        
        tournament.runTournament()

        try:
            winner = tournament.rounds[-1].matches[0].winner.name
        except IndexError:
            print("Something went wrong when simulating a tournament, no winner was found.")
            break
    
        winCounts[winner] += 1

    return {team: count/numSimulations for team, count in winCounts.items()}

# helper function
def getTeamNames(tournament):
    return [team.name for team in tournament.teams]

# helper function
def initializeWinCounts(teamNames):
    return dict.fromkeys(teamNames, 0)