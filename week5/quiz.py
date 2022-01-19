# ask user questions and tally if they get it right

user_input = input('Would you like to play the game? yes or no ')

if(user_input != 'yes'):
    quit()

user_input = input('What is your age? ')

if(int(user_input) < 21):
    print('sorry, you are not old enough')
else:
    print('welcome')
