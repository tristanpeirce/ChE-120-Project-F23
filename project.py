# Group Members: Tristan Peirce (TP), William Cook (WC), Andrew Al (AA), Austin Drew (AD)
# Student IDs (respectively): 21076017, 21107176, 21101134, 21093469

import random

def instructions():
    print('''\n🐷 Welcome to Pig 🐷
\nHow To Play:
    🐽 Players take turns rolling the dice
    🐽 The first person to reach 100 points wins
    🐽 If a player rolls a '1', their turn ends and they lose all the points they earned that turn
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
    
    
def hand_display(player):
    print('\nPlayer %s\'s Turn' %(player + 1))
    print('Your Points: %s' %(get_total(player)))

def get_total(player):
    total = 0
    
    for i in players[player]:
        total += i
    return total

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
    
    roll_question = input('\nWould you like to roll the dice (y/n)? ')
    while True:
        if roll_question.lower() == 'y':
            if roll(whos_turn) != 1:
                roll_question = input('\nWould you like to roll the dice (y/n)? ')
                if roll_question.lower() == 'n':
                    break
                elif not (roll_question.lower() == 'y'):
                    roll_question = input('\nInvalid input! Please enter \'y\' or \'n\': ')
            else:
                break
        elif roll_question.lower() == 'n':
            break
        else:
            roll_question = input('\nInvalid input! Please enter \'y\' or \'n\': ')
    
    if get_total(whos_turn) >= 100:
        print('\n🥓 Player %s is the winner 🥓' %(whos_turn + 1))
        break
    
    if whos_turn == (num_players - 1):
        whos_turn = 0
    else:
        whos_turn += 1