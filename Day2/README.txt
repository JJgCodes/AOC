--- Day 2: Rock Paper Scissors ---

Sample data ; 
For example, suppose you were given the following strategy guide:

A Y
B X
C Z

"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" 
Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
Winning every time would be suspicious, so the responses must have been carefully chosen.

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

puzzleData ; 
P1:
What would your total score be if everything goes exactly according to your strategy guide?

Result = 10404

P2:

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
you would get a total score of 12.


Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

Result = 10334.


Reflection;

Better way would be some kind of inversion of data rather than explicitly defining each game type.
