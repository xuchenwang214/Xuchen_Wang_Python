# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:51:57 2016

@author: xuchenwang
"""

# Question 8: Guess number game
'''Guess number game

   Users can input a number between 1 to 20. It will show if it is correct on the 
   screen and give some clues.
'''
# input user's name
name = input('Hello! What is your name?')
# tell user what to do
print('Well,',name,' I am thinking of a number between 1 and 20.')
# real number
real = 18
# give the time user guessed an initial value
time = 1
# use while loop to let user have a guess
while True:
    # input user's guess
    guess = int(input('Take a guess,'))
    # if the guess number is high, give a clue
    if guess > real:
        print('Your guess is too high.')
        # guess time increase
        time+=1
    # if the guess number is low, give a clue
    elif guess < real:
        print('Your guess is too low.')
        # guess time increase
        time+=1
    else:
        # if the guess is correct, print the guess times
        print('Good job, ',name,'! You guessed my number in',time,'guesses!')
        break