# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:36:37 2016

@author: xuchenwang
"""
# Question 9: anagram
'''anagram

   A random chose word of permutation of a colour shows on the screen. The user
   can make a guess of the colour word.
'''
# import random library
import random
# given a list of colour
color = ['red','green','yellow','orange','white','brown','black','grey','purple']
# randomly choose a colour
co_choose = random.choice(color)
# convert str to a list
li = list(co_choose)
# use shuffle to randomly permute the list
random.shuffle(li)
# convert the list to str
new_word = ''.join(li)
# print the new word to the user
print('Colour word anagram: ',new_word)
# use loop to let user take a guess
while True:
    # let user input his guess
    word_guess = input('Guess the colour word!')
    # if user guess the word, over and shows correct, if not, continue to guess
    if word_guess == co_choose:
        print('Correct!')
        break
    





