import random
def greet():
    print('Welcome to guess the number game!\n')
    name = input('Enter your name here:- ')
    print(f'Hello {name}')

def game():
    maxn = 100
    n = random.randint(1, maxn)
    print('Guess the number from 1 to %d' % maxn)
    guess = None
    while guess != n:
        guess = int(input('Your try: '))
        if guess > n:
            print('Too high')
        if guess < n:
            print('Too low')

    print('Congratulations, you won!')
greet()
game()
