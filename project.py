# Group Members: Andrew Al (AA), William Cook (WC), Austin Drew (AD), Tristan Peirce (TP)
# Student IDs (respectively): 21101134, 21107176, 21093469, 21076017

import random # imports the random module for use in the roll function (TP)
import sys # imports the sys module for the ability to quit the program (TP)
import time # imports the time module for the ability to delay the program quitting (TP)

def instructions(): # this function will print the instructions to inform the player on how to play the game (WC)
    '''
    () -> NoneType
    
    This function, when ran, will print the instructions for playing the game Pig (WC).
    '''
    print('''\n🐷 Welcome to Pig 🐷
\nHow To Play:
    🐽 Players take turns rolling the dice
    🐽 The first person to reach 100 points wins
    🐽 Players may roll as many times as they'd like during their turn
    🐽 If a player rolls a '1', their turn ends and they lose all the points they earned that turn
    🐽 A Player may enter quit at any point to exit the game
    ''')

def valid_int_input(num):
    if num.isnumeric() and (num <= '6' and num >= '2'):
        return True
    else:
        return False
    
def roll(player):
    print()
    dice = []
    rolled = random.randint(1,6)
    dice.append(rolled)
    for line in range(5):
        for i in dice:
            print(dice_art.get(i)[line], end="")
        print()
    if rolled == 1:
        print('You rolled a %s! Your turn is over :(' %(rolled))
        players[player] = old_total
    else:
        print('You rolled a %s!' %(rolled))
        players[player].append(rolled)
    return rolled
    
    
def hand_display(player): # function for displaying the amount of points and turn of a given player (AD)
    '''
    (int) -> NoneType
    
    Displays the current player's turn and total points (AA).
    '''
    print('\nPlayer %s\'s Turn' %(player + 1)) # prints which players turn it is, adds one to player index in players list in order to display the corrct player number (AD)
    print('Your Points: %s' %(get_total(player))) # prints the amount of points the given player has, using the get_total function in order to do so (AD)

def get_total(player): # this function takes an input of the player number and gets their total score based on their dice rolls (WC)
    '''
    (int) -> int
    
    Sums up a player's total points and returns that total for display (AA).
    '''
    total = 0 # Sets the total for the player to 0 (WC)
    
    for i in players[player]: # initiates a for loop that will add every number of each die rolled to a total variable (WC)
        total += i # adds the numbers rolled to the total (WC)
    return total # returns the new total the player acheived during their turn based on their dice rolls (WC)

players = [] # creates an empty list for which each player indicated playing the game in 'num_players' will have there own list inside the list which keeps track of their score (AA)
playing = True # assigns 'playing' to True so that when running the 'while: playing' loop, it will run until it encounters a break (AA)
whos_turn = 0 # starts the game at player 1 (AA)
dice_art = { # dictionary is to provide visual feedback to the player for which number they roll by indexing into the dictionary the random integer they get between 1 and 6 (AA)
    1: ("┌─────────┐", # die image for a rolled value of 1 (AA)
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐", # die image for a rolled value of 2 (AA)
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐", # die image for a rolled value of 3 (AA)
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐", # die image for a rolled value of 4 (AA)
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐", # die image for a rolled value of 5 (AA)
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐", # die image for a rolled value of 6 (AA)
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

instructions() # displays instructions from the 'instructions' function at the top (AA)

num_players = input('How many people are playing? ') # asks the user(s) how many players are participating in the game and provides them a space to input their answer (AA)
while valid_int_input(num_players) != True: # checks to see if the number of players inputted is not within the game's boundaries (2-6) (AA)
    num_players = input('\nInvalid input! Please enter a number between 2 and 6.\nHow many people are playing? ') # if the input does not meet the requirements, than the user(s) are prompted to try again to input a valid number of players (AA)
if valid_int_input(num_players): # ensures that the number of players is valid gievn the parameters (AA)
    num_players = int(num_players) # converts the numeric string to an int type (AA)
for i in range(num_players): # assigns multiple lists (one for each player) with 0 as the only value into the previous empty 'players' list, where 0 represents each players score at the time of starting the game (AA)
    players.append([0])

while playing: # initializes the start of the game that will continue until someone has won or the game has been quit (TP)
    
    old_total = players[whos_turn].copy() # creates a copy of the players total points before their turn in case they roll a 1, which allows for their points to then be reset back to this total (TP)
    hand_display(whos_turn) # calls the function 'hand_display' to display whos turn it is and that players points (TP)
    
    roll_question = input('\nWould you like to roll the dice (y/n or quit)? ') # prompts the player to input whether they would like to roll the die, end their turn, or quit the game (TP)
    while True: # loop that allows the player to keep rolling over and over again until a 1 is rolled, they quit the game, or decide not to roll again (TP)
        if roll_question.lower() == 'quit': # if the player wishes to quit the game, a quitting message is printed and after a delay the program is quit (TP)
            print('\nQuitting game...')
            time.sleep(1)
            sys.exit()
        elif roll_question.lower() == 'y': # if the player wishes to roll the die, the following code is executed (TP)
            if roll(whos_turn) != 1: # if the die rolled is not a 1, it prompts the user to input whether they would like to roll again, end their turn or quit (TP)
                roll_question = input('\nWould you like to roll the dice (y/n or quit)? ')
                if roll_question.lower() == 'n': # if they wish to end their turn, it will break from the loop ending their turn (TP)
                    break
                elif not (roll_question.lower() == 'y' or not roll_question.lower() == 'quit'): # if the player's next input is not 'y', 'n', or 'quit', it prompts the user for another input (TP)
                    roll_question = input('\nInvalid input! Please enter \'y\', \'n\' or \'quit\': ')
            else: # if the die rolled is a 1, it will break from the loop ending the players turn (TP)
                break
        elif roll_question.lower() == 'n': # if the player wishes to end their turn, it will break from the loop ending their turn (TP)
            break
        else: # if the user provides an invalid input, they are prompted to input a correct input (TP)
            roll_question = input('\nInvalid input! Please enter \'y\', \'n\' or \'quit\': ')
    
    if get_total(whos_turn) >= 100: # if the player ends their turn with a point total of 100 or more, they win the game (TP)
        print('\n🥓 Player %s is the winner 🥓' %(whos_turn + 1)) # a winning statement is printed and after a delay, the loop is broken and the game has ended (TP)
        time.sleep(1)
        break
    
    if whos_turn == (num_players - 1): # if it is the last players turn, then it goes back to player 1 (TP)
        whos_turn = 0
    else: # if it is anyone else's turn, the game moves to the next player (TP)
        whos_turn += 1
