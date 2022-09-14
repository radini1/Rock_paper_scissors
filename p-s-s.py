import random

while True:
    m = input('paper , scissors or stone ? ')
    v2 = ['stone', 'paper', 'scissors']
    
    if m == 'paper':
        v = random.choice(v2)
        if v == 'stone':
            print(f'you won! computer selected {v}'); print('if you dont want to continue the game, type (bye).')
        elif v == 'scissors':
            print(f'you loose! computer selected {v}'); print('if you dont want to continue the game, type (bye).')
        else:
            print(f'draw! computer selected {v}'); print('if you dont want to continue the game, type (bye).')
            
    elif m == 'stone':
        v = random.choice(v2)
        if v == 'stone':
            print('draw'); print('if you dont want to continue the game, type (bye).')
        elif v == 'scissors':
            print('you won!'); print('if you dont want to continue the game, type (bye).')
        else:
            print('you loose!'); print('if you dont want to continue the game, type (bye).')
            
    else:
        v = random.choice(v2)
        if v == 'stone':
            print('you loose!'); print('if you dont want to continue the game, type (bye).')
        elif v == 'scissors':
            print('draw!'); print('if you dont want to continue the game, type (bye).')
        else:
            print('you won!'); print('if you dont want to continue the game, type (bye).')
            
    if m == 'bye':
        me = input('how many times did you win ? ')
        com = input('how many times did bot win? ')
        if me > com:
            print('you were better!')
        else:
            print("computer was better!")          
        break 
    