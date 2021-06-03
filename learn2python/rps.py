import random, sys


print('Rock, Paper, Scissors')

# These variables keep track of the wins, losses, and ties
wins=0
losses=0
ties=0

while True: #the main game loop
    print('%s Wins, %s Losses %s Ties' % (wins, losses, ties))
    while True: #the player input loop
        print('Enter your move: r rock p paper s scissors or q quit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print ('type one of r, p, s, or q')

    #display what player chose
    if playerMove =='r':
        print('Rock versus...')
    if playerMove =='p':
        print('Paper versus...')
    if playerMove =='s':
        print('Scissors versus...')

    #display what computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove='r'
        print('rock')
    if randomNumber == 2:
        computerMove='p'
        print('paper')
    if randomNumber == 3:
        computerMove='s'
        print('scissors')
    
    #diplay and record score
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties +1
    elif playerMove == 'r' and computerMove=='s':
        print('You win!')
        wins = wins +1
    elif playerMove == 'p' and computerMove=='r':
        print('You win!')
        wins = wins +1
    elif playerMove == 's' and computerMove=='p':
        print('You win!')
        wins = wins +1
    elif playerMove == 'r' and computerMove=='p':
        print('You lose!')
        losses = losses +1
    elif playerMove == 'p' and computerMove=='s':
        print('You lose!')
        losses = losses +1
    elif playerMove == 's' and computerMove=='r':
        print('You lose!')
        losses = losses +1
    
    