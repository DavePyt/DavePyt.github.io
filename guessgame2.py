import random


def get_the_number_of_attempts(attempts):  # this function gets the number of attempts

    while True:
        try:

            attempts = int(input(' Please re-enter the number of attempts you wish to have(3-10 attempts): \n >'))

            if attempts <= 10 and attempts >= 1:
                return attempts
            else:
                print(f'{attempts} is not between the range')

        except ValueError:
            print('Invalid input... not an integer')


guess_number = random.randint(1, 10)
attempts= 0
attempts_num = get_the_number_of_attempts(attempts)
count = 0
guesslimit_reached = False
guess = 0

while guess != guess_number and not guesslimit_reached:
    guess = int(input('Guess a number between 1 and 10: \n >'))
    if guess < guess_number:
        print ('your guess is low')
    elif guess> guess_number:
        print('your guess is high')

    count += 1
    if count == attempts_num:
        guesslimit_reached = True

if guess == guess_number:
        print(f' Congratulations, you guessed it on {count} attempts')

else:
    print(f'You maxed out your number of attempts. I was thinking of {guess_number}')