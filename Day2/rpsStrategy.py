import csv

def getData():
    gamePlay = []
    with open('day2/inputdata.txt') as fd:
        reader = csv.reader(fd)
        for row in reader: 
           gamePlay.append(row)
            
    return gamePlay

# not required to have words associated with inputs but for my approach and readability have done so
opponentDictionary = {
    'A': 'ROCK', 
    'B': 'PAPER',
    'C': 'SCISSORS'
}

playerDictionary = {
    'X': 'ROCK', 
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

results = {
    'Z': 6,
    'X': 0,
    'Y': 3,
}

points = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}

#  not the best way could be improved. 
def checkResults(opponent, player):
    if opponent == 'ROCK' and player == 'Y':
        return 'ROCK'
    elif opponent == 'ROCK' and player == 'Z':
        return 'PAPER'
    elif opponent == 'ROCK' and player == 'X':
        return 'SCISSORS'
    
    if opponent == 'PAPER' and player == 'Y':
            return 'PAPER'
    elif opponent == 'PAPER' and player == 'Z':
        return 'SCISSORS'
    elif opponent == 'PAPER' and player == 'X':
        return 'ROCK'
    
    if opponent == 'SCISSORS' and player == 'Y':
            return 'SCISSORS'
    elif opponent == 'SCISSORS' and player == 'Z':
        return 'ROCK'
    elif opponent == 'SCISSORS' and player == 'X':
        return 'PAPER'
    
    # if opponent  == rock and player == y
    #  return draw and rock
 



def playGame(game):
    playerScore = 0
    for play in game:
        opponentPlays = opponentDictionary.get(play[0][0])
        playerPlays = play[0][-1]
        outcome = checkResults(opponentPlays,playerPlays)
        playerScore += points.get(outcome) + results.get(playerPlays)
        
    return playerScore
        
        
outcome = playGame(getData())

print(outcome)