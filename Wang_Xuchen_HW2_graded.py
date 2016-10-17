# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:01:21 2016

@author: xuchenwang
"""

'''Question 1. Fibonacci sequence
  
   The first function calculates the nth term of the Fibonacci sequence.
   The second function returns the index of the first tern in the Fibonacci
   sequence to contain a given digits.
'''

def fibonacci(n): 
    # Creat a list of Fibonacci sequence and initial the first two numbers.
    F = [1,1]
    # Use the formula for Fibonacci sequence to calculate the nth term.
    for i in range(2,n):    
        F.append(F[i-1]+F[i-2])
    # Print the nth term.
    print (F[n-1])

def index_digit(digit):
    # Creat lists of the Fibonacci sequence and the length of each number. Give the first two elements.
    F = [1,1]
    Len = [1,1]
    # 'i' is the index of terms in the seq.
    i = 2
    # The while loop will stop once the digit is equal to 100
    while len(str(F[i-1]))< 100:
        # Calculate the nth term in each list.
        F.append(F[i-1]+F[i-2])
        Len.append(len(str(F[i])))
        # After calculation, increase the index to next term.
        i +=1
    # Print the index.
    print(i)
# check
fibonacci(47)   
index_digit(100)




'''Question 2. Total maximum

   Given a triangle, this function find the maximum total from top to bottom.
'''

triangle= [ [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]   ]

def max_triangle(triangle):
    '''
    The loop starts from the last second line, each number in this line plus the 
    bigger one of its adjacent numbers so that each outcome stands for the maximum
    total from this line to bottom. Repeat this process up to the top line, then 
    the top element is the maximum total from top to bottom.
    '''
    n = len(triangle)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    print('The maximum total from top to bottom is ',triangle[0][0])

max_triangle(triangle)




'''Question 3. Collatz Promblem

   The first function calculates the length of the Collatz chain for a given number.
   The main function return the starting number that produces the longest chain under
   a given number.

'''

def collatz(num):
    # Initial the length as 1.
    length = 1
    # The chain will stop once the number equals 1.
    while num != 1:
        # If it is an even number, the next one equals num/2.
        if num%2 == 0:
            num = int(num/2)
        # Otherwise, if it is an odd number, the next one equals 3*num+1
        else:
            num = 3*num+1
        # Each time, when finish the caculation for the next number in the chain, the length would increase 1.
        length += 1
    # The return value is the length of chain.
    return length
    
def main(upper_limit):
    # Initial the value of length.
    value = collatz(1)
    # Initial the starting number.
    start = 1
    # Use for loop to go through every positive integer under the upper_limit
    for i in range(2,upper_limit):
        # If the length of number i is bigger than value, change the value to the bigger one and change the starting number.
        if value < collatz(i):
            value = collatz(i)
            start = i
    # Print the result.
    print('Starting number {}, under {}, produces the longest chain and the length is {}'.format(start,upper_limit,value))
    
main(1000)



        
'''Question 4. Recurring cycle for an given integer

   This function can output the length of recurring cycle for an given integer.
   And maximum of length that it could calculate is 600. That means if the length 
   of the recurring cycle is bigger than 600, it just returns 0.
   For d<500, it could print the number which has the longest recurring cycle.
'''

#Stuart- Interesting solution and correct, but if you wanted to run this program 
#on integers greater than 2000 your code would fail. If you decided not to call 
#any external lbiraries you could try implementing long division from scratch, but
#this solves the problem as asked.


# Use getcontext() function in decimal library to improve the digit after '.' to 2000 digits.
from decimal import *
getcontext().prec = 2000

# Define a function, ‘integer’ stands for the denominator.
def recur_cycle(integer):   
    # x is the result of 1/integer with 2000 digits after '.'
    x = Decimal(1)/Decimal(integer)
    # Convert number x to string.
    temp = str(x)
    # Find the position of '.' in temp
    place = temp.find('.')
    # Remove '.' and digits before '.'
    temp = temp[place+1:]
    # Initial i as 1 and define running as a sign
    i = 1
    running = True
    # The while loop will stop once the 'running' change to false.
    while running:
        # If there is digit which recurred twice, then i should be the length of recurring cycle and finish the loop.
        if temp[:i] == temp[i:2*i] and temp[i:2*i]== temp[2*i:3*i]:
            return i
            running = False
        # If i increase to 600, stop the loop and recognize the length as 0.
        elif i == 600:
            return 0
            running = False
        # If i is not the length of recurring cycle and i is smaller than 600, add 1 to i and go on to the next loop.
        else:
            i +=1

def main():
    # define an empty list for the length 
    length = []
    # calculate every length for integer from 2 to 499 and add it to the list           
    for i in range(2,500):
        length.append(recur_cycle(i))
    # print the max length of the list
    print ('The integer which has the longest recurring cycle is {}. Its length is {}.'.format(length.index(max(length))+2,max(length)))

main()




'''Question 5. Ways of currency

   This function returns how many differnt ways a curtain sum_total can be made
   using any number of coins in a given list of coins.
'''

def currency(coin,sum_total):
    '''
    Creat a 'coin_way[kind][sums]' list-- 'sums' means the currency we want to get and 
    'kind' means how many kinds of coins we use to get sums.
    The first row which means we only use '1p' to get sums, so the way is always equals 1.
    The first col which means we use some kinds of coin to get 0. It should be 0. But here
    we suppose it to be 1 in order to do calculation followed.
    
    If we want to get coin_way[i][sums], compare to last row i-1, it just add one kind of 
    coin. For this kind of coin, there is sums/coin[i] ways. So if we do not use this coin,
    there is coin_way[i-1][sums] ways. If we use this coin once, there is coin_way[i-1][sums-1*coin[i]]
    ways. If we use this coin twice, there is coin_way[i-1][sums-2*coin[i]] ways and so on.
    We have the formula:
    coin_way[i][sums] = coin_way[i-1][sums-0*coin[i]]+coin_way[i-1][sums-1*coin[i]]+......
                        +coin_way[i-1][sums-(sums/coin[i])*coin[i]]
    (Note: if we use (sums/coin[i]) times of coin[i], which means we only use coin[i] to get sums,
           it is one way. That's why we need to initial the first col as 1. )
           
    Thus, the last element in the list is what we want.    
    '''
    kind_total = len(coin)
    # Creat a list.
    coin_way = [([0] * (sum_total+1)) for i in range(kind_total)]
    # Initial the first row and the first col.
    for i in range(sum_total+1):
        coin_way[0][i] = 1
    for i in range(kind_total):
        coin_way[i][0] = 1
    # Use the formula above.
    for kind in range(1,kind_total):
        for sums in range(1,sum_total+1):
            for k in range(int(sums/coin[kind]+1)):
                coin_way[kind][sums] += coin_way[kind-1][sums-k*coin[kind]]
    # Print the last one as the result
    print('There are {} ways £2 can be made.'.format(coin_way[-1][-1]))

currency([1,2,5,10,20,50,100,200],200)   




'''Question 6. Check prime

   This function takes a positive integer and checks if it is prime.
'''

#Stuart- While yes this does determine if a number is prime this is not a recursive program.
#Remember recursive programs are ones that call for the running of themselves inside their code.


def check_prime(integer):
    # Creat a list for prime numbber. The first prime is 2. 
    prime = [2]
    # Make a sign.
    running = True
    # The first positive number which need to check is 3.
    num = 3
    # The while loop will stop once running change to false.
    while running:
        # If the integer is 2, since it is already in the list, over the loop.
        if integer == 2:
            running = False
        # This var. is used to count the number of true for the following 'for' loop.
        time_true = 0
        # If num could not be divided by prime[i], increase 1 to time_true.        
        for i in range(len(prime)):
            if num%prime[i] != 0:
                time_true += 1
        # If the num could not be divided by all of the prime smaller than itself, it is a prime and add it to the prime list.
        if time_true == len(prime):
            prime.append(num)
        # We do not need to check the positive integer larger than 'integer'.
        if num == integer:
            running = False
        # If num is smaller than 'integer', move on to next positive integer and go on to the next loop.
        else:
            num +=1
    # if integer is in prime list, then it is a prime.
    if integer in prime:
        print(integer,'is a prime')
    else:
        print(integer,'is not a prime')
#check
check_prime(127)




'''Question 7. Sort a list of strings

   Given a list of strings. This function can sort it by the following rules:
   1. The order is number 0-9 first and then letter a-z (regardless of lowercase
      or uppercase).
   2. If the first character is the same, then compare the second one. If the second
      character is the same, compare the third one and so on.
   3. If two strings have the same first several characters, then the shorter one
      comes first. (e.g. 'car' and 'carpool', 'car' comes first)
'''
#Stuart- A nice sorting algorithm implementation, but again, not recursive.

# strings is a list of strings
def sort_list(strings):
    '''
    Use Bubble Sort method: compare each pair of two adjacent strings,
    if the former one is bigger than the later one, exchange them. So in the 
    first time, the biggest one should be at the end of the list. Next time,
    repeat the same process expect for the last one. Repeat several times till
    the list is sorted.
    '''
    for times in range(1,len(strings)):
        for i in range(len(strings)-times):
            # n is the length or shorter string, we can only compare the first n characters.
            n = min(len(strings[i]),len(strings[i+1]))
            flag = 0
            for j in range(n):
                # If the character is not the same, they should be sorted. Put the bigger one in the later position and break the loop.
                if strings[i][j] != strings[i+1][j]:
                    if strings[i][j]>strings[i+1][j]:
                        temp = strings[i]
                        strings[i] = strings[i+1]
                        strings[i+1] = temp
                    break
                # If the characters are the same, add 1 to 'flag'.
                elif strings[i][j] == strings[i+1][j]:
                    flag +=1
            # If flag is equal to n, then it follows the third rule. Put the shorter one in the former position.
            if flag == n and len(strings[i])>len(strings[i+1]):
                strings[i] = strings[i+1]
    print(strings)
    
# check
strings = ['rd','bosg','gage','gages','ras','vrdsaf','hiasu','3afa']            
sort_list(strings)  




'''Question 8. Recursion of a function

   This function shows the result of recursion of the expression 3.95x(1-x) for
   n times. The input x should be in [0,1].
'''
def fun_cycle_1(x,n):
    # define the expression 3.95x(1-x)
    def f(x):
        return 3.95*x*(1-x)
    # rerun the expression for n times
    for i in range(n):
        x = f(x)
    print(x)

def fun_cycle_2(x,n):
    # define the expression 3.95x-3.95x^2
    def f(x):
        return 3.95*x-3.95*x*x
    # rerun the expression for n times
    for i in range(n):
        x = f(x)
    print(x)

def fun_cycle_3(x,n):
    # define the expression 3.95(x-x^2)
    def f(x):
        return 3.95*(x-x*x)
    # rerun the expression for n times
    for i in range(n):
        x = f(x)
    print(x)
    
fun_cycle_1(0.9,100) # result:  0.9230225584410336
fun_cycle_2(0.9,100) # result:  0.9714692195380887
fun_cycle_3(0.9,100) # result:  0.3078187619897856
'''
The results are different because the number of type 'float' only has 17 digits.
For differnt expressions of the same function, the order of calculation is different.
So each time, they get different return value. And this value is the input next time.
In other words, the input in next time is different. Through 100 times calculation,
the results are totally distinct.
'''













