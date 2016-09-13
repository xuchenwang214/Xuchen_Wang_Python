# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:04:54 2016

@author: xuchenwang
"""

# Question 10: lingo
'''lingo

   Users can enter a five long word. Some clues about the word will show on the 
   screen. 
'''
# The true word
lingo = 'tiger'
# use while loop to let user take a guess
while True:
    # let user input the word
    word = input('')
    # convert str to list
    li_lingo = list(lingo)
    li_word = list(word)
    # if user gets the word, print it and break
    if lingo == word:
        print('[t][i][g][e][r]')
        break
    # if not, search every position of the word and give some clues
    for i in range(len(li_word)):
        # if user have both the right char. and the right position, add a '[]'
        if li_word[i] == li_lingo[i]:
            seq = ('[',li_word[i],']')
            li_word[i] = ''.join(seq)
            print(li_word[i])
        # if user only get the right char., add a '()'
        elif li_word[i] in lingo:
            seq1 = ('(',li_word[i],')')
            li_word[i] = ''.join(seq1)
    # convert list to str
    clue = ''.join(li_word)
    # print the clue to the user
    print('Clue: ',clue)
    
        


