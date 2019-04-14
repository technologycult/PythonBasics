'''
Python 3 Basics - Session # 11

Topic to be covered - While Loops in Python 3

a. Syntax of While Loop
b. Syntax of While Else
c. Debugging While Loop
d. Create a game with While Loop
'''

i = 0

while i < 5:
    print('My name is Khan!')
    i +=1
else:
    print('In the Else Section')
print('End Line')

###############################################################################
import random
runs_required = 25
no_balls_left = 6

runs_scored = 0
ball_count=1

while no_balls_left > 0:
    print('*******************************************')
    print('No of Balls Faced :', ball_count)
    #runs_per_ball = int(input('enter the runs scored'))
    runs_per_ball = random.randint(0,6)
    print('Runs Scored in this ball :', runs_per_ball)
    runs_scored += runs_per_ball
    no_balls_left -=1
    print('Number of Balls Left :', no_balls_left)
    print('Total Runs Scored :',runs_scored)
    print('Runs Required to win :', runs_required - runs_scored)
    ball_count +=1
    if runs_scored  > runs_required:
        print('Batting Team won')
        break;
else:
    print('Bowling Team won')
        


























 