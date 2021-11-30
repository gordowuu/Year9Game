import getUserInfo as info
from art import *
import time
import playsound
from pygame import mixer
import textgamelib
import random
#clear console
textgamelib.clearConsole()
#title
titleArt = text2art("Clue Breakout", font="small")
starCount = 0

def collaborationStar():
    global starCount
    print("⭐")
    playsound.playsound('./Year9Game/music/star.mp3')
    print("You currently have", starCount, "collaboration stars.")



print("                         Welcome to \n" + titleArt +"\n                     An escape room game \n                      Made by Gordon Wu")
print("")
time.sleep(1.6)
infoList = info.getUserInfo()

print ("Hello", infoList[0],"you have been invited to participate in the Clue Breakout")
time.sleep(2)
print("In this game you will be trying to escape multiple rooms by solving puzzles.\nAt the end of the game you want to collect 5 collaboration stars.")
print("Each collaboration star looks like this:")
collaborationStar()

#room1

def box():
    global boxOpen
    global starCount
    print("As you kneel down to look at the big box you realize there is a 2 slot code lock. You have to find 2 numbers that will open the lock. Maybe something behind the doors will give you the code.")
    testLock = input("Do you want to test the lock? type y for yes or n for no:")
    print(testLock)
    if testLock.lower() == "y":
        print("The lock has 2 slots that you can spin for numbers.")
        slot1 = input("What is the code for slot 1?:")
        if slot1 == "9":
            print("The lock clicked when you spun to 9, this mean you got the right answer!")
        else:
            print("The lock did not click when you spun to",slot1,",this means it is not the right answer.")
        slot2 = input("What is the code for slot 2?")
        if slot2 == "6":
            print("The lock clicked when you spun to 6, this means you got the correct answer!")
        else:
            print("The lock did not click when you spun to",slot2,",this means it is not the right answer.")
        if slot1 == "9" and slot2 == "6":
            boxOpen = True
            print("Good job you broke the code!\nNow you open the box and realize there is a colaboration star inside of it. But also under the star is a hole with a ladder.")
            print("You pick up the collaboration star and suddenly it disapears and turns into lots of glitter.")
            starCount += 1
            collaborationStar()
        else:
            print("Return to the box if you would like to try again.")
    if testLock.lower() == "n":
        print("Your stand up from the box.")
        


        
   

def door1():
    print("You walking up to door 1 and it is open, you walk through and on the wall is a black board.\nOn the black board it says: Solve 2 + 15 - 8")
    door1 = (input("What is the answer to the question?:"))
    while door1 != "9":
        print("You write", door1, "on the black board and suddenly the board starts speaking\nThe blackboard says, Try again!")
        door1 = (input("What is the answer to the question?:"))
    if door1 == "9":
         print("You write 9 on the black board and suddenly it starts speaking\nThe blackboard says, Good Job! Now LEAVE THIS ROOM! I NEED TO SLEEP! You quickly run out and close the door behind you.")
         

def door2():
    print("You walk into door 2 and on the wall you find an old grandfather clock.\nYou notice that the minute hand is at 12, and the hour hand is at 6" )
    mixer.init()
    mixer.music.load('./Year9Game/music/clock.mp3')
    mixer.music.play()
    door2 = (input("What time is it? (write the number, for example 2 not two) :"))
    while door2 != "6":
        print("You say",door2,"o clock out loud and suddenly the clock comes to life.\n Mr. Clock says: HEY THAT NOT MY CURRENT TIME, try again (make sure you type with numbers not letters")
        door2 = (input("What time is it?:"))
    if door2 == "6":
        print("You say 6 out loud and suddenly the clock comes to life.\nMr. Clock says: Nice, finally someone that can actually understand me, NOW SCRAM I NEED TO MOVE MY HANDS! \nSo you walk back out into the main room.")
        
    mixer.music.stop()

boxOpen = False
while boxOpen == False:
    room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2): ")
    print(room1)
    if room1.upper() == "B":
        box()
    if room1 == "1":
        door1()
    if room1 == "2":
        door2()


#room2 
Alan = "Alan is a 11 year old Chinese boy that loves to read books and code. He is very smart and is very observant."
Claire = "Claire is a 12 year old Canadian girl that loves to eat food and draw. She is very creative and has good eyesight"
Ishir = "Ishir is a 10 year old Indian boy that loves to play sports like soccer and tennis. He is very strong and fast."
friendList = [Alan, Claire, Ishir]
while boxOpen == True:
    time.sleep(2)
    print("You go down the ladder and find your self in a small room with table. On the table is a telephone and a note.")
    print("You grab the note and on the note it says:\nThis magic telephone will allow you to call one of the other children that have escaped room 1. They can help you escape the other rooms but you don't have to work with them.")
    print("When you answer the phone they will be introduce but if you don't want to work with them ignore the phone.")
    phoneChoice = input("Do you want to call the phone? y/n:").lower()

    if phoneChoice == "y":
        print("You call the magical phone and suddenly someone answers the phone.")
        friend1 = random.randint(1,3)
        room2Difficulty = True
        if friend1 == 1:
            print(Alan)
        elif friend1 == 2:
            print(Claire)
        else:
            print(Ishir)
        print("You decided that you want to work with a friend. You suddenly feel fuzzy and feel a tingle because you realize you are being teleported.")
    
    if phoneChoice == "n":
        room2Difficulty = False
        print("You decided that you want to escape alone. You suddenly feel fuzzy and feel a tingle because you realize you are being teleported.")

# def room2WithFriend():
    





    


