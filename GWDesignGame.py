import getUserInfo as info
from art import *
import time
import playsound
from pygame import mixer
#title
titleArt = text2art("Clue Beakout", font="small")
starCount = 0
def collaborationStar():
    print("⭐")
    playsound.playsound('./music/star.mp3')
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
print("You wake up in a small black room, with a backpack and nothing else.\nAs you look around, you realize there is a small blue box, and three closed doors. The doors are labelled 1, 2 and 3.")

    
room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")
print(room1)

if room1 == "B":
    print("As you kneel down to look at the small box you realize there is a 3 slot code lock. You have to find 3 numbers that will open the lock so you stand back up.")
    room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")
    
if room1 == "1":
    print("You walking up to door 1 and it is open, you walk through and on the wall is a black board.\nOn the black board it says: Solve 2 + 15 -8")
    door1 = int(input("What is the answer to the question?:"))
    while door1 != 9:
        print("You write", door1, "on the black board and suddenly the board starts speaking\nThe blackboard says, Try again!")
        door1 = int(input("What is the answer to the question?:"))
    if door1 == 9:
         print("You write 9 on the black board and suddenly it starts speaking\nThe blackboard says, Good Job! Now LEAVE THIS ROOM! I NEED TO SLEEP! You quickly run out and close the door behind you.")
         room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")

if room1 == "2":
    print("You walk into door 2 and on the wall you find an old grandfather clock.\nYou notice that the minute hand is at 12, and the hour hand is at 6" )
    mixer.init()
    mixer.music.load('./music/clock.mp3')
    mixer.music.play()
    door2 = int(input("What time is it? (write the number, for example 2 not two) :"))
    while door2 != 6:
        print("You say",door2,"o clock out loud and suddenly the clock comes to life.\n Mr. Clock says: HEY THAT NOT MY CURRENT TIME, try again")
        door2 = int(input("What time is it?:"))
    if door2 == 6:
        print("You say 6 out loud and suddenly the clock comes to life.\nMr. Clock says: Nice, finally someone that can actually understand me, NOW SCRAM I NEED TO MOVE MY HANDS! \nSo you walk back out into the main room.")
        room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")
    mixer.music.stop()

if room1 == "3":
    print("In room 3 you find a simple riddle written in a book. Beside the book you find a pencil.\nThe book says:\nWhat goes up but never come back down?")
    door3 = input("What is the answer to the riddle?:")
    while "age" in door3.lower():
        print("You write",door3,"in the book and the book randomly starts speaking.\nAlmost boy, think about one of the beginning questions.")
        door3 = input("What is the answer to the riddle?")
    if door3 == infoList[1]:
        print("Wow, you know your own age, amazing!\nYou return to the main room.")
    else:
        print("The book says try again")
        door3 = input("What is the answer to the riddle?")



    


