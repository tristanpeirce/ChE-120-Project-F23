# Group Members: Tristan Peirce (TP), William Cook (WC), Andrew Al (AA), Austin Drew (AD)
# Student IDs (respectively): 21076017, 21107176, 21101134, 21093469

import random
import sys
import time

def instructions(): # This function will print the instructions to infor the player on how to play the game (WC)
    '''
    () -> NoneType
    
    This function, when ran, will print the instructions for playing the game pig (WC)
    '''
    print('''\n🐷 Welcome to Pig 🐷 # This print statement will appear as soon as the file is run to inform the user on how to play the game as well as the  (WC)
\nHow To Play:
    🐽 Players take turns rolling the dice
    🐽 The first person to reach 100 points wins
    🐽 Players may roll as many times as they'd like during their turn
    🐽 If a player rolls a '1', their turn ends and they lose all the points they earned that turn
    🐽 A Player may enter quit at any point to exit the game
    ''')
    return None # The function returns nothing, the only thing that appear when this function is ran is the print statement above (WC)

def valid_int_input(num): # This function will validate the input for how many players are playing when the code prompts it (WC)
    '''
    (int) -> boolType
    
    This function takes an input num and returns True if the input is numeric and is in between 2 and 6 and returns False otherwise (WC)
    '''
    if num.isnumeric() and (num <= '6' and num >= '2'): # This if statement checks the input to ensure it is a number between 2 and 6 (WC)
        return True # returns True if the input satisfies the requirements (WC)
    else: # If the input is anything else other than a number between 2 and 6 (WC)
        return False # The function reutrns false if the input does not satisfy the requirements (WC)
    
def roll(player): # function for when a die is rolled (AD)
    print() # blank print statement to generate a new line, purely for aesthetics (AD)
    dice = [] # creates an empty list assigned to variable "dice", in order to display what the dice rolls later on (AD)
    rolled = random.randint(1,6) # Generates a random integer between 1 and 6 to represent the rolling of a die, assigns this generated value to variable "rolled" (AD)
    dice.append(rolled) # appends the number assigned to rolled into the list dice, allowing the dice to be drawn later on (AD)
    for line in range(5): # loop that repeats 5 times. The art for the dice have 5 lines to print each. This allows the die to be printed line by line (AD)
        print(dice_art[rolled][line]) # prints the dice art for the rolled value that coensides with the dictionary for the dice art line by line (AD)
    if rolled == 1: # if the number assigned to rolled is 1, meaning the players turn is forced to be over one (AD)
        print('You rolled a %s! Your turn is over :(' %(rolled)) # Prints statement telling player they rolled a 1, ending their turn (AD)
        players[player] = old_total # resets current player list of die rolls inside of 2-D list "players" to what it was before their turn started (AD)
    else: # if the number assigned to rolled is anything but a 1, meaning the playes turn can continue if they wish (AD)
        print('You rolled a %s!' %(rolled)) # prints statement telling plater what they rolled (AD)
        players[player].append(rolled) # appends the value assigned to rolled into the current player list inside of 2-D list "players" (AD)
    return rolled # returns the value assigned to rolled for later use in the program (AD)
    
    
def hand_display(player): # function for displaying the amount of points and turn of a given player (AD)
    print('\nPlayer %s\'s Turn' %(player + 1)) # prints which players turn it is, adds one to players index in player list in order to displayv the corrct player number (AD)
    print('Your Points: %s' %(get_total(player))) # prints the amount of points the given player has, using the get_total function in order to do so (AD)

def get_total(player): # This function takes an input of the player number and gets their total score based on their dice rolls (WC)
    total = 0 # Sets the total for the turn to 0 (WC)
    
    for i in players[player]: # initiates a for loop that will add every number rolled to a total variable (WC)
        total += i # Adds the numbers rolled to the total (WC)
    return total # Returns the new total the player acheived during their turn based on their dice rolls (WC)

players = []
playing = True
whos_turn = 0
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

instructions()

num_players = input('How many people are playing? ')
while valid_int_input(num_players) != True:
    num_players = input('\nInvalid input! Please enter a number between 2 and 6.\nHow many people are playing? ')
if valid_int_input(num_players):
    num_players = int(num_players)
for i in range(num_players):
    players.append([0])

while playing:
    
    old_total = players[whos_turn].copy()
    hand_display(whos_turn)
    
    roll_question = input('\nWould you like to roll the dice (y/n or quit)? ')
    while True:
        if roll_question.lower() == 'quit':
            print('\nQuitting game...')
            time.sleep(1)
            sys.exit()
        elif roll_question.lower() == 'y':
            if roll(whos_turn) != 1:
                roll_question = input('\nWould you like to roll the dice (y/n or quit)? ')
                if roll_question.lower() == 'n':
                    break
                elif not (roll_question.lower() == 'y' or roll_question.lower() == 'quit'):
                    roll_question = input('\nInvalid input! Please enter \'y\', \'n\' or \'quit\': ')
            else:
                break
        elif roll_question.lower() == 'n':
            break
        else:
            roll_question = input('\nInvalid input! Please enter \'y\', \'n\' or \'quit\': ')
    
    if get_total(whos_turn) >= 100:
        print('\n🥓 Player %s is the winner 🥓' %(whos_turn + 1))
        time.sleep(1)
        break
    
    if whos_turn == (num_players - 1):
        whos_turn = 0
    else:
        whos_turn += 1
