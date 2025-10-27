# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 

import random 

def game():
    score = random.randint(1,100)
    return score

# Read the previous high score 
with open("game.txt", "r") as f:
    content = f.read().strip()

if content == "":
    hi_score = 0
else:
    hi_score = int(content)

# Play the game
current_score = game()

# Compare and update the high score if needed
if current_score > hi_score:
    print("New High Score!", current_score)
    print("High score was:", hi_score)
    with open("game.txt", "w") as f:
        f.write(str(current_score))
else:
    print("Your score:", current_score)
    print("High score remains:", hi_score)
