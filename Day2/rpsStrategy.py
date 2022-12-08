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
    'WIN': 6,
    'LOSS': 0,
    'TIE': 3,
}

points = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}

#  not the best way could be improved. 
def checkResults(opponent, player):
    if opponent == player:
        return 'TIE'
    elif opponent == 'ROCK' and player == 'SCISSORS':
        return 'LOSS'
    elif opponent == 'ROCK' and player == 'PAPER':
        return 'WIN'
    elif opponent == 'PAPER' and player == 'ROCK':
        return 'LOSS'
    elif opponent == 'PAPER' and player == 'SCISSORS':
        return 'WIN'
    elif opponent == 'SCISSORS' and player == 'PAPER':
        return 'LOSS'
    elif opponent == 'SCISSORS' and player == 'ROCK': 
        return 'WIN'
 



def playGame(game):
    playerScore = 0
    for play in game:
        opponentPlays = opponentDictionary.get(play[0][0])
        playerPlays = playerDictionary.get(play[0][-1])
        outcome = checkResults(opponentPlays,playerPlays)
        playerScore += results.get(outcome) + points.get(playerPlays)
        
    return playerScore
        
        
outcome = playGame(getData())


print(outcome)