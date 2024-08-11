import random
m=['rock','paper','scissor']
def sam():
    while True:
        print('**********************************************************************')
        s = input('ENTER YOUR OPTION LIKE [ROCK,PAPER,SCISSOR] ').lower()
        print(f'YOUR OPTION IS {s}')
        w = random.choice(m)
        print(f'COMPUTER OPTION IS {w}')

        if (s == 'paper' and w == 'rock') or (s == 'rock' and w == 'scissor') or (s == 'scissor' and w == 'paper') or (s == 'scissor' and w == 'paper') :
            print('you won')
            game()
            break

        elif (s == 'scissor' and w == 'scissor') or (s == 'paper' and w == 'paper') or (s == 'rock' and w == 'rock'):
            print('The game is Draw')
            game()
            break

        else:
            print('play again ,you loss the game')

print('WELCOME TO THE [ROCK,PAPER,SCISSOR] GAME')
print('*******************************************')
def game():
    print('*******************************************')
    e=input('Are u willing to play the game say yes/no  ').lower()
    while True:
        if e=='yes':
            sam()

            break
        else:
            print('THANK FOR PLAYING THIS GAME')
            break
game()