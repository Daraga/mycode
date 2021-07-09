#!/usr/bin/env python3


from colorama import Fore, Back, Style  # allows color and style change


import random   #allowws you to use random 

#move list for both characters
move_list = ("attack", "block", "grab", "special")

#health counters for both characters
P1health = 1
P2health = 1
health1 = ("Your health is")
health2 = ("Your opponent health is ")


#opening statement
print(random.choice(move_list))
input ("\nWelcome to BATTLEGROUND! Your battle begins now!  \nPress enter to continue")

#rules explanation
input ("\nYou both start off with 1 health, pick the correct move in order to defeat your foe. \nPress enter to continue\n")

print (*move_list, sep="\n")    #show move list

while True:
    move1 = input("\nInput a move from your move list: ")
   
    if move1 =='attack':
        print ('\33[1m' + Fore.GREEN + "\nYour opponent tries to grab you but you punch them in the face" +'\33[1m')    #adds color and bold to text
        print (Style.RESET_ALL)     #stops color change
        P2health = P2health - 1
        P1health = P1health + 0
        print (health1)
        print (P1health) 
        print (health2)
        print (P2health)

        if P2health==0:
            print ('\33[1m' + "\nYOU WIN" + '\33[0m')
            break

    if move1 =="grab":
        print ('\33[1m' + Fore.CYAN + "\nYou try to grab your opponent but youre met with a swift boot to the face" + '\33[1m')
        print (Style.RESET_ALL)
        P2health = P2health - 0
        P1health = P1health - 1
        print (health1)
        print (P1health) 
        print (health2)
        print (P2health)
            
        if P1health==0:
            print ('\33[1m' + "\nGAME OVER" + '\33[0m')
            break
    
    if move1 =="block":
        print ('\33[1m' + Fore.CYAN + "\nYour opponent's body seems to flash as he leaps towards you with a bicycle kick that seems to last way too long. you hold your arms up to block the kicks but it does reduced damage" + '\33[1m')
        print (Style.RESET_ALL)
        P2health = P2health - 0
        P1health = P1health - 1
        print (health1)
        print (P1health) 
        print (health2)
        print (P2health)
            
        if P1health==0:
            print ('\33[1m' + "\nGAME OVER" + '\33[0m')
            break

    if move1 =='special':
        print ('\33[1m' + Fore.GREEN + "\nYou feel a surge of energy bursting forth. You punch the ground 3 times, energy waves burst through towards your opponent. He raises his arms to block but to no avail." +'\33[1m')
        print (Style.RESET_ALL)
        P2health = P2health - 1
        P1health = P1health + 0
        print (health1)
        print (P1health) 
        print (health2)
        print (P2health)

        if P2health==0:
            print ('\33[1m' + "\nYOU WIN" + '\33[0m')
            break

    
    else:
        print ('\33[1m' + Fore.YELLOW + "\nYou have input the wrong move. Please try again" + '\33[1m')  
        print (Style.RESET_ALL)
        print (*move_list, sep="\n")
