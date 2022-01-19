# simple rock papper scissors, tally for computer versus human
# will need to add randomization for computer

import random

computer_score = 0
user_score = 0

# rock = 0, paper = 1, scissors = 2
options_arr = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock, paper, scissors, or q to quit.\n').lower()
    if(user_input == 'q'):
        break
    elif(user_input in options_arr):
        random_number = random.randint(0, 2)
        print('Computer picked ' + options_arr[random_number])
        # tie
        if(random_number == options_arr.index(user_input)):
            print('tie')
        # cases when user wins
        elif(
        user_input == 'rock' and random_number == 2 or
        user_input == 'paper' and random_number == 0 or
        user_input == 'scissors' and random_number == 1
        ):
            user_score += 1
            print('You won!')
        # no tie, user loses, computer wins
        else:
            computer_score += 1
            print('You lost')
    else:
        print('error: incorrect option, try again')

print('User Score: ' + str(user_score))
print('Computer Score: ' + str(computer_score))
