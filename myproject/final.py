#!/usr/bin/env python3

from colorama import Fore, Back, Style  # allows color and style change

import random   #allows you to use random 

import os

#move list for both characters
moves = ("attack", "dodge", "special")

#character HP
P1HP = 5
P2HP = 5
count = 0
# function to show remaining health
def showHP():
    print('\33[1m' +Fore.GREEN + "Your HP = " +str(P1HP) +'\33[1m')
    print (Style.RESET_ALL)
    print ('\33[1m' + Fore.CYAN + "Foes HP = " + str(P2HP) + '\33[1m')
    print (Style.RESET_ALL)


#Have P1 lose 1HP
def loseP1():
    global P1HP
    P1HP = P1HP -1
    print ('\33[1m' + Fore.BLUE + "\nYou take 1 dmg" +'\33[1m')    #adds color and bold to text
    print (Style.RESET_ALL)     #stops color change

#Have P2 lose 1 HP
def loseP2():
    global P2HP
    P2HP = P2HP - 1
    print ('\33[1m' + Fore.BLUE + "\nYour foe takes 1 dmg" + '\33[1m')
    print (Style.RESET_ALL)     #stops color change

def cheat():
    global count
    count = count + 1



#opening statement
input ("\nWelcome to Battleground. Execute moves to overtake your foe. Victory is in your grasp  \nPress enter to continue: ")
print (f"\nType in one of the available moves. You both start with {P1HP} health\n")
#print (*moves, sep="\n")

while True:
    
    print (*moves, sep="\n")
    atk = input("\nWhich move will you use: ")
    foeatk = (random.choice(moves))
    os.system('clear')

    if atk == "attack" and foeatk == "dodge":
        print ("\nYour oppenent tries to concentrate but a swift strike knocks them off balance")
        loseP2()
        showHP()
    
    elif atk =='attack' and foeatk == "special" :
        print ("\nYou try to attack your oponent but their body flashes with energy blinding you. While trying to regain your vision, an energy wave slams into you")
        loseP1()
        showHP()
        
    elif atk =='dodge' and foeatk == "special" :
        print ("\nYou watch your foe, on guard, as they fire an energy blast at you, you skillfully dofge and counter with a kick")
        loseP2()
        showHP()
    
    elif atk =='dodge' and foeatk == "attack" :
        print ("\nYou try to focus on dodging your opponents next move but their attack turns out to be a feint, while off balance your foe kicks you, knocking you down")
        loseP1()
        showHP()

    elif atk =='special' and foeatk == "attack" :
        print ("\nYou charge up a kinetic energy. Your foe realizes what youre doing and attacks you. Your foe is too late and you punch the ground sending energy waves towards your foe")
        loseP2()
        showHP()
    
    elif atk =='special' and foeatk == "dodge" :
        print ("\nYou begin charging your energy. You fire off a ball of energy as your foe rushes towards you and redirects your attack back into you")
        loseP1()
        showHP()
    
    elif atk == foeatk:    #what happens on ties
        print ("\nYou and opponent move in the same way as if dancing in a mirror. Both of you decide to back off, neither of you managing to score a hit")
        print ('\33[1m' + Fore.BLUE + "\nYou got a TIE" +'\33[1m')    #adds color and bold to text
        print (Style.RESET_ALL)     #stops color change
        showHP()
            
    else:
    #elif atk !=moves:
        cheat()
        if count ==1:
            print('\33[1m' + Fore.YELLOW + "\nYou attempt a skill that you do not know and end up on the floor. Your opponent watches you flail in confusion" +'\33[1m')
            print(Style.RESET_ALL)
            
        
        if count ==2:
            print('\33[1m' + Fore.YELLOW + "\nYour opponent watches you fail an attack again. Their wariness decreases " +'\33[1m')
            print(Style.RESET_ALL)

        if count ==3:
            print('\33[1m' + Fore.YELLOW + "\nAs you fail your attack this time, Your opponent decides that you\'re an idiot and delivers a quick kick to your butt " +'\33[1m')
            print(Style.RESET_ALL)
            loseP1()
            showHP()
            count = 0



    if P2HP == 0:
        print('\33[1m' + Fore.YELLOW + "\nCONGRATULATIONS. YOU DEFEATED YOUR ARCH NEMESIS" +'\33[1m')
        break
    
    if P1HP == 0:
        print('\33[1m' + Fore.YELLOW + "\nYOU HAVE BEEN DEFEATED! TRAIN HARDER AND TRY AGAIN" +'\33[1m')
        break
