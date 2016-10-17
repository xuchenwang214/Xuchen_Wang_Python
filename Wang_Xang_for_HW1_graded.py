#Stuart- As part of your documentation you should include the purpose (in the help format) and inputs to
#each of the major functions that you write (~one per problem) you have the information just not as part of the
#function
#Stuart- Any points lost due to lack of documentation or using script instead of functions
# can be regained if the issues are corrected. Please email me once you have corrected the issue
# and I will check your code.
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:14:32 2016

@author: xuchenwang
"""


# Question 1: Palindrome Recogniser
''' Palindrome Recogniser

    Users can enter the name or the path of a file. This recogniser will show
    if each line of the file is palindrome. Pay attention: this recogniser does
    not overlook space and punctuations.
'''
#Stuart- Need additional documentation. When you print you are printing a word at a time
#and not a line at a time.

# define a new function
def palindrome(name):
    # Open the file.
    import string
    file = open(name) 
    # Read and split each line in the text.
    readline = file.read().split() 
    # Use for loop to judge if each line is palindrome. If it is, show it on the screen.
    for frontword in readline: 
        for backword in readline:
            if frontword == backword[::-1]:
                print(frontword)
# Use the defined function. Users can input the name or the path of a file.
palindrome(input('What is your file name?') )


# Question 2: Semordnilap Recogniser
''' Semordnilap Recogniser

    Users can enter a file name(pointing to a list of words--assume that there
    is only space between the words). Then the recogniser can find pairs of words
    that is semordnilap and shows it on the screen.
'''

#Stuart- when you run this problem on a file with multiple lines you will see that
#the '\n' at the end of each line keeps the program from recognizing the semordnilaps
#try simply using file.read().split()

# define a new function
def semordnilap(name):
    # Open the file
    file = open(name)
    # Read the file and split each word by space
    words = file.read().split(' ')
    # Use two loops to compare every pair of words. Judge if they are semordinilap and shows them on the screen.
    for i in range(len(words)):
        for j in range(i,len(words)):
            if words[i] == words[j][::-1]:
                print(words[i],' ',words[j])
# Use the defined function. Users can input the name or the path of a file.
semordnilap(input('What is your file name?') )    


# Question 3: Frequency Table
'''Frequency Table

   Users can enter a file name. And a table of frequency of character 'a' to 'z',
   ',','.','?','!' will show on the screen.
'''
# define a new function
def char_freq_table(name):
    # Open the file
    file = open(name)
    # Read the file and convert every uppercase to its lowercase.
    passage = file.read().lower()
    # Creat a list of character.
    char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z',',','.','?','!']
    # Use str.count fun. to count the frequency of each character and print the table.
    for i in range(len(char)):
        print(char[i],' ',passage.count(char[i]))
# Use the defined function. Users can input the name or the path of a file.
char_freq_table(input('What is your file name?') )      


# Question 4: ICAO Speaker
'''ICAO Speaker

   Users can enter a file of passage. The speaker will translate it into ICAO words.
   Users can also choose the length of pause between each ICAO words and each words 
   in the passage.
'''
# define a new function. The default length of pause are 1s and 3s each.
def speak_ICAO(name, float_icao = 1, float_word = 3):
    # import library os and time.
    import os
    import time
    # creat the icao dictionary
    d = { 'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
      'g':'golf', 'h':'hotel', 'i': 'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
      'm':'mike', 'n': 'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
      's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
      'y':'yankee', 'z':'zulu'}
    # Open the file.  
    file = open(name)
    # Read and convert uppercase to lowercase.
    word = file.read().lower()
    # Overlook punctuation in the passage.
    for pun in ('!','?',',','.',"'",'"',':'):
        word = word.replace(pun,'')
    # Ignore '\n' 
    word = word.replace('\n',' ')
    # Split every words
    word = word.split(' ')
    # Use for loops to translate every alphabet to icao words and speak.
    for i in range(len(word)):
        # Make a pause between each words.
        time.sleep(float_word)
        for j in range(len(word[i])):
            for alph, icao in d.items():
                # translate every alphabet in the word to icao words and access to TTS to speak.
                if word[i][j] == alph:
                    os.system('say '+icao)
                    # Make a pause between each icao words.
                    time.sleep(float_icao)
# Use the defined function. Users can input the name or the path of a file and choose the length of pause.
speak_ICAO(input('What is your file name?') )           


# Question 5. Hapax Recongniser
'''Hapax Recongiser

   Users can enter the name of a text file. The recogniser will show every hapax
   (word only appears one time in the text).
'''
# define a new function.
def hapax(name):
    # Open the file.  
    file = open(name)
    # Read and convert uppercase to lowercase.
    word = file.read().lower()
    # Overlook punctuation in the passage.
    for pun in ('!','?',',','.',"'",'"',':'):
        word = word.replace(pun,'')
    # Ignore '\n' 
    word = word.replace('\n',' ')
    # Split every words
    word = word.split(' ')
    # Use for loop to count the time of each word appears.
    for i in range(len(word)):
        # if the word only appears once, print it on the screen.
        if word.count(word[i]) == 1:
            print(word[i])
# Use the defined function. Users can input the name or the path of a file.
hapax(input('What is your file name?') )


# Question 6: Numbered Text File
'''Numbered Text File

   Users can enter the name of a file. The function will creat a new file and 
   number each line in the old file.
'''
# define a new function
def numbered_file(name):
    # open the file
    file = open(name)
    # read the file and split each line
    lines = file.read().split('\n')
    for i in range(len(lines)):
        # insert number before each line
        lines.insert(3*i,str(i+1))
        # insert \n after each line
        lines.insert(3*i+2,'\n')
    # create a new file    
    new_file = open('new_file.txt','w')
    # write the new list lines in the file
    for i in range(len(lines)):
        new_file.writelines(lines[i])
    # close the file
    new_file.close()
# Use the defined function. Users can input the name or the path of a file.
numbered_file(input('What is your file name?') )


# Question 7: Calculate average length of word
'''Calculate average length of word

   Users can enter the name of a file. The function can return the average length 
   of the word stored in the file.
'''
#Stuart- If you add a print statement for word at the very last step you might see a '' as
# the last entry (if you pressed ENTER after last word in file or have trailing ' ') this is because the split created
#a trailing empty string 

# define a new function
def cal_aver(name):
    # Open the file.  
    file = open(name)
    # Read and convert uppercase to lowercase.
    word = file.read().lower()
    # Overlook punctuation in the passage.
    for pun in ('!','?',',','.',"'",'"',':'):
        word = word.replace(pun,'')
    word = word.replace('\n',' ')
    # Split every words
    word = word.split(' ')
    # creat a var. to store the length of total words
    sum_total = 0
    # Use for loop to add length of each word to the sum_total.
    for i in range(len(word)):
        sum_total += len(word[i])
    # show the average length of word
    print(sum_total/len(word))
# Use the defined function. Users can input the name or the path of a file.
cal_aver(input('What is your file name?') )


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

#Stuart- This should be a random number. Look at the random library.

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
    
    
# Question 10: lingo
'''lingo

   Users can enter a five long word. Some clues about the word will show on the 
   screen. 
'''
#Stuart- Could use additional documentation

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


# Qusetion 11. Sentence Splitter
'''Sentence Splitter

   Split sentences by '.''?''!', except for some special conditions
'''
#Stuart- Excellent use of regular expressions, but you need to put this in function form.

import re
text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
# use re.split to split sentences except for certain conditions.
m = re.split('(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s' , text)

for i in m :
    print(i + '\n')
    
# Qusetion 12. 
import defaultdict

#Stuart- I had to edit the code myself because I received an indentation error on your documentation in
# quotes. Be careful because python is very particular about indentation. The way you called the print function
# also does not work for python 3. Python 3 calls it differently than 2.7
def anagram(name):
	# get every word from the list and store them in wordbank
	wordbank = []
	with open(name) as file:
		for line in file:
			wordbank.append(line.rstrip())
      '''
      use defaultdict fun. to creat a dic and the key is the same characters that
      the words share. The value is every word that shares the same char.
      '''
	dict_anagram = defaultdict(list)
	for word in wordbank:
		key = ''.join(sorted(word))
		dict_anagram[key].append(word)

	# give length an initial value as 0
	length = 0
     # find the largest length
	for word1, word2 in anadict.items():
		if len(word2) > length:
			length = len(word2)

	# print the anagrams with the largest length
	for word1, word2 in anadict.items():
		if len(word2) > length-1:
			print word1, word2

#test
anagram('wordlist.txt')

# Question 13(1)
'''Generate and balance

   Generate a string with N '[' and N ']' and judge if it consists entirely of 
   pairs of brackets
'''
# import library random
import random
# define a function to generate a string, parameter N stands for how many pairs
def generate(N):
    # creat a list to store brackets
    li = [' ']*(2*N)
    # Since there are 2N elements, randomly select N position to store '['
    for i in range(N):
        a = random.randint(1,N*2)
        li[a] = '['
    # The rest of the list is ']'
    for i in range(N*2):
        if li[i] == ' ':
            li[i] = ']'
    # convert the list to a string
    string = ''.join(li)
    # return string 
    return string

# define a function to check if the string is balance
def balance(string):
    '''for the pair of brackets: if we encounter a '[', num plus 1; if we encounter
       a ']', num minus 1. Since the sequence of bracket is always '['']', when we get
       a negative num, the bracket is unbalanced.(It is impossible to have more ']' than
       '[' if it is balanced.) So when num is negative, break the loop and print 'NOTOK'.
       When the final outcome of num is 0, it is balanced.
    '''
    num = 0
    for i in range(len(string)):
        if string[i] == '[':
            num += 1
        else:
            num -= 1
        if num < 0:
            break
    if num == 0:
        print(string,'OK')
    else:
        print(string,'NOT OK')
# check the condition when N=4
balance(generate(4))

#Stuart- Run your code multiple times. You will see that in generate you will periodically
# get a list assignment index out of range error. Remember lists are numbered [0,n-1].

# Question 13(2) Pokemon Game
'''Pokemon Game

   Given a list of pokemon words, generate a list of highest possible number of 
   Pokemon name.
'''
pokelist = ["audino","bagon","baltoy","banette","bidoof", "braviary", "bronzor", 
"carracosta","charmeleon","cresselia", "croagunk", "darmanitan", "deino", "emboar",
"emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus", "heatmor", 
"heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan","kricketune", "landorus", 
"ledyba", "loudred", "lumineon", "lunatone", "machamp", "magnezone", "mamoswine",
"nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath", "poochyena", 
"porygon2","porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye", 
"scolipede", "scrafty", "seaking","sealeo", "silcoon", "simisear", "snivy", "snorlax",
"spoink", "starly", "tirtouga", "trapinch", "treecko","tyrogue", "vigoroth", "vulpix",
"wailord", "wartortle","whismur","wingull" ,"yamask"]
# Create a final list
finallist = []
# define a function to generate the sequence with highest possible numbers of Pokemon names
def search(newlist):
    global pokelist,finallist
    # use flag as a sign
    flag = 0
    # Use a for loop
    for name in pokelist:
        # check if the list is empty or it could followed by another word
        if ((len(newlist) == 0) or ((name[0] == newlist[-1][-1]) and (name not in newlist))):
            # if so, add the name into the list and turn the flag as another num, such as 1
            flag = 1
            newlist.append(name)
            # search for the next word
            search(newlist)
            # delete the last word to search for other conditions
            newlist.pop()
    # when flag is 0, means there is no words to enter into the list
    if flag == 0:
        # compare the length of each list, finallist is the longest one
        if (len(newlist)>len(finallist)):
            finallist = list(newlist)

def main():
    global finallist
    search([])
    # print the final list on the screen
    print (len(finallist),'The elements are',finallist)
    
main()


# Question 14. Alternade
'''Alternade

   Split every word in the list with strict order.
'''
file = open('/Users/xuchenwang/Desktop/wordlist.txt')
# read and split the file
wordbank = file.read().split()
# use for loop to go through every word
for word in wordbank:
    
    smallword_1 = ''
    smallword_2 = ''
    word_1 = ''
    word_2 = ''
    # check if the length of word is 1, if so, it makes no word
    if len(word) == 1:
        print(word,': makes no word.') 
    # if not, store every word in even position in smallword1 and every word in odd position in smallword2
    else:
        for i in range(len(word)):
            if i%2 == 0:
                smallword_1 = smallword_1 + word[i]
            else:
                smallword_2 = smallword_2 + word[i]
        # check if every smallword is in wordbank, if so, store and print it on the screen
        for j in range(len(wordbank)):
            if smallword_1 == wordbank[j]:
                word_1 = wordbank[j]
            elif smallword_2 == wordbank[j]:
                word_2 = wordbank[j]                
        if (word_1 != '' and word_2 != ''):  
            print(word,' makes ',word_1,' and ',word_2,'\n')














