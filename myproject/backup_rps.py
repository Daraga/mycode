#!/usr/bin/env python3

from colorama import Fore, Back, Style  # allows color and style change

import random   #allows you to use random 

#move list for both characters

RPS = ("rock", "paper", "scissors")
win = 0
lose = 0

#print (random.choice(RPS))

#opening statement
input ("\nReady for a game of Rock, Paper, Scissors?  \nPress enter to continue")

print ("\nWhat will you throw out\n")
print (*RPS, sep="\n")    #show move list

while True:
    throw1 = input("\n What will you throw?: ")
    foethrow = (random.choice(RPS))
   
    if throw1 =='rock' and foethrow == "scissors" :
        print ("\nYou threw " + throw1 + " and they threw " + foethrow)
        print ('\33[1m' + Fore.BLUE + "\nYou win" +'\33[1m')    #adds color and bold to text
        print (Style.RESET_ALL)     #stops color change
        win = win + 1
        print('\33[1m' +Fore.GREEN + "Your wins = " +str(win) +'\33[1m')
        print (Style.RESET_ALL)
        print ('\33[1m' + Fore.CYAN + "Your losses = " + str(lose) + '\33[1m')
        print (Style.RESET_ALL)
    
    elif throw1 =='rock' and foethrow == "paper" :
        print ("\nYou threw " + throw1 + " and they threw " + foethrow)
        print ('\33[1m' + Fore.BLUE + "\nYou lose" +'\33[1m')    #adds color and bold to text
        print (Style.RESET_ALL)     #stops color change
        lose = lose + 1
        print('\33[1m' +Fore.GREEN + "Your wins = " + str(win) +'\33[1m')
        print (Style.RESET_ALL)
        print ('\33[1m' + Fore.CYAN + "Your losses = " + str(lose) + '\33[1m')
        print (Style.RESET_ALL)

    elif throw1 =='paper' and foethrow == "rock" :
        print ("\nYou threw " + throw1 + " and they threw " + foethrow)
        print ('\33[1m' + Fore.BLUE + "\nYou lose" +'\33[1m')    #adds color and bold to text
        print (Style.RESET_ALL)     #stops color change
        lose = lose + 1
        print('\33[1m' +Fore.GREEN + "Your wins = " + str(win) +'\33[1m')
        print (Style.RESET_ALL)
        print ('\33[1m' + Fore.CYAN + "Your losses = " + str(lose) + '\33[1m')
        print (Style.RESET_ALL)
    
    elif throw1 == foethrow:
        print ("\nYou threw " + throw1 + " and they threw " + foethrow)
        print ('\33[1m' + Fore.BLUE + "\nYou got a TIE" +'\33[1m')    #adds color and bold to text
        print (Style.RESET_ALL)     #stops color change
        print('\33[1m' +Fore.GREEN + "Your wins = " + str(win) +'\33[1m')
        print (Style.RESET_ALL)
        print ('\33[1m' + Fore.CYAN + "Your losses = " + str(lose) + '\33[1m')
        print (Style.RESET_ALL)
            
    elif throw1 !=RPS:
        print('\33[1m' + Fore.YELLOW + "\nCheating will not be tolerated. Try again" +'\33[1m')
        print(Style.RESET_ALL)

