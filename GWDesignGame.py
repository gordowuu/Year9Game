import getUserInfo as info
from art import *
import time
from pygame import mixer
import textgamelib
import random
#clear console
textgamelib.clearConsole()
#title
titleArt = text2art("Clue Breakout", font="small")
starCount = 0
gameOver = text2art("Game Over", font="small")

def collaborationStar():
    global starCount
    print("⭐")
    mixer.init()
    mixer.music.load('./Year9Game/music/star.mp3')
    mixer.music.play()
    print("You currently have", starCount, "collaboration stars.")
    mixer.music.stop()



print("                         Welcome to \n" + titleArt +"\n                     An escape room game \n                      Made by Gordon Wu")
print("")
time.sleep(1.6)
infoList = info.getUserInfo()

print ("Hello", infoList[0],"you have been invited to participate in the Clue Breakout")
time.sleep(2)
print("In this game you will be trying to escape multiple rooms by solving puzzles.\nAt the end of the game you want to collect 3 collaboration stars.")
print("Each collaboration star looks like this:")
collaborationStar()

#room1
print("You start in room 1. Alone and lost. You notice that there is a big box in the middle of the room and 2 doors behind it.")
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
    print("You walk up to door 1 and it is open, you walk through and on the wall is a black board.\nOn the black board it says: Solve 2 + 15 - 8")
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
def room2WithFriend():
    global boxOpen
    global starCount
    print("You some how end up in another room. This time with a whiteboard on the wall and your new friend",friend1Name)
    print("On the whiteboard, someone wrote:\nRiddle me this! What goes up but never comes down.")
    correct = False
    incorrectScore = 0
    riddleAnswer = input("What is the answer to the question?:")
    while correct == False:
        if "age" in riddleAnswer:
                print("The whiteboard says: Almost there, think a little deeper!")
                riddleAnswer = input("What is the answer to the question?:")
                incorrectScore += 1
        elif riddleAnswer == infoList[1]:
            incorrectScore = 0
            print(friend1Name,"says: Good job! We did it")
            print("The whiteboard hands you a collaboration star!")
            starCount += 1
            collaborationStar()
            time.sleep(1)
            print("Suddenly a dark mysterious man appears before your eyes!")
            boxOpen = False
            correct = True
        else:
            print("The whiteboard says: Not quite, please try again!")
            riddleAnswer = input("What is the answer to the question?:")
            incorrectScore += 1
        if incorrectScore == 1:
            print(friend1Name, "says: OH I think I have heard of this riddle before. I think the answer is your age. Your age always goes up but never comes down!")
        elif incorrectScore == 3:
            print(friend1Name, "says: WOW now it makes sense to me, think about the first few question when we first started this game.")
        
        
        
def room2WithOutFriend():
    global boxOpen
    global starCount
    print("You some how end up in another room. This time with a whiteboard on the wall.")
    print("On the whiteboard, someone wrote:\nRiddle me this! What goes up but never comes down.")
    correct = False
    riddleAnswer = input("What is the answer to the question?:")
    incorrectScore = 0
    while correct == False:
        if "age" in riddleAnswer:
                print("The whiteboard says: Almost there, think a little deeper!")
                riddleAnswer = input("What is the answer to the question?:")
                incorrectScore += 1
        elif riddleAnswer == infoList[1]:
            print("Good job! You did it")
            print("The whiteboard hands you a collaboration star!")
            starCount += 1
            collaborationStar()
            time.sleep(1)
            print("Suddenly a dark mysterious man appears before your eyes!")
            boxOpen = False
            correct = True
        else:
            print("The whiteboard says: Not quite, please try again!")
            riddleAnswer = input("What is the answer to the question?:")
            incorrectScore += 1
        
        if incorrectScore > 4:
            correct = True
            boxOpen = False
            print("Your marker has ran out of ink.")
            print(gameOver)
            print("You finished the game but didn't escape.")
            print("Your finished the game with a total of ",starCount,"Collaboration Stars\n Thanks for playing!")

        

    

        


Alan = "Alan is a 11 year old Chinese boy that loves to read books and code. He is very smart and is very observant."
Claire = "Claire is a 12 year old Canadian girl that loves to eat food and draw. She is very creative and has good eyesight"
Ishir = "Ishir is a 10 year old Indian boy that loves to play sports like soccer and tennis. He is very strong and fast."
friendList = [Alan, Claire, Ishir]

while boxOpen == True:
    time.sleep(2)
    print("You go down the ladder and find your self in a small room with table. On the table is a telephone and a note.")
    print("You grab the note and on the note it says:\nThis magic telephone will allow you to call one of the other children that have escaped room 1. They can help you escape the other rooms but you don't have to work with them.")
    print("When you answer the phone they will be introduced but if you don't want to work with them ignore the phone.")
    phoneChoice = input("Do you want to call the phone? y/n:").lower()

    if phoneChoice == "y":
        print("You call the magical phone and suddenly someone answers the phone.")
        friend1 = random.randint(1,3)
        hasFriend = True
        if friend1 == 1:
            print(Alan)
            friend1Name = "Alan"
        elif friend1 == 2:
            print(Claire)
            friend1Name = "Claire"
        else:
            print(Ishir)
            friend1Name = "Ishir"

    if phoneChoice.lower() == "y":
        time.sleep(2)
        print("You decided that you want to work with a friend. You suddenly feel fuzzy and feel a tingle because you realize you are being teleported.")
        room2WithFriend()
    
    if phoneChoice.lower() == "n":
        time.sleep(2)
        print("You decided that you want to escape alone. You suddenly feel fuzzy and feel a tingle because you realize you are being teleported.")
        room2WithOutFriend()

#room3
print("The man says: Hello",infoList[0],". I challenge you to a game of rock paper scissors.\nI have 5 lives and everytime you beat me I lose one life. If you defeat me I will let you escape.")
accept_challenge = input("Do you accept the challenge? y/n:")
boss_bar =  ['❤️','❤️','❤️','❤️','❤️']
player_health = ['❤️','❤️','❤️']
room3Start = False
room3StartWithoutFriend = False
def gameEnd():
    print("Thank you for playing! You finished the game with",starCount,"Collaboration Stars.")
if accept_challenge.lower() == "n":
    print(gameOver)
    print("You finished the game but didn't escape.")
    print("Your finished the game with a total of ",starCount,"Collaboration Stars\n Thanks for playing!")
elif accept_challenge.lower() == "y":
    if phoneChoice == "y":
        room3Start = True
    elif phoneChoice == "n":
        room3StartWithoutFriend = True

while room3Start == True:
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    if computer_action == "rock":
        randChoice = random.randint(1,2)
        if randChoice == 1:
            print(friend1Name,"whispers in your ear that he thinks the man will go rock.")
        else:
            print(friend1Name,"whispers in your ear that he thinks the man will go scissors.")
    if computer_action == "paper":
        randChoice = random.randint(1,2)
        if randChoice == 1:
            print(friend1Name,"whispers in your ear that he thinks the man will go paper.")
        else:
            print(friend1Name,"whispers in your ear that he thinks the man will go rock.")
    if computer_action == "scissors":
        randChoice = random.randint(1,2)
        if randChoice == 1:
            print(friend1Name,"whispers in your ear that he thinks the man will go scissors.")
        else:
            print(friend1Name,"whispers in your ear that he thinks the man will go paper.")
    

    user_action = input("Enter a choice (rock, paper, scissors): ")
    print("\nYou chose", user_action, "computer chose", computer_action,"\n")

    if user_action == computer_action:
        print("Both players selected", user_action,". It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            boss_bar.pop(0)
            print("The man now has",boss_bar,"health.")
        else:
            print("Paper covers rock! You lose.")
            player_health.pop(0)
            print("You now have",player_health,"health.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            boss_bar.pop(0)
            print("The man now has",boss_bar,"health.")
        else:
            print("Scissors cuts paper! You lose.")
            player_health.pop(0)
            print("You now have",player_health,"health.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            boss_bar.pop(0)
            print("The man now has",boss_bar,"health.")
        else:
            print("Rock smashes scissors! You lose.")
            player_health.pop(0)
            print("You now have",player_health,"health.")

    if boss_bar == []:
        print("The man says: Congratulations, you have defeated me. You may now exit the game and escape.")
        time.sleep(1)
        print("But before you go please take this.\nThe mysterious man hands you a Collaboration star")
        starCount += 1
        collaborationStar()
        gameEnd()
        room3Start = False
    elif player_health == []:
        print(gameOver)
        print("You finished the game but didn't escape.")
        print("Your finished the game with a total of ",starCount,"Collaboration Stars\n Thanks for playing!")
        room3Start = False



while room3StartWithoutFriend == True:
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    print("\nYou chose", user_action, "computer chose", computer_action,"\n")

    if user_action == computer_action:
        print("Both players selected", user_action,". It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            boss_bar.pop(0)
            print("The man now has",boss_bar,"health.")
        else:
            print("Paper covers rock! You lose.")
            player_health.pop(0)
            print("You now have",player_health,"health.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            boss_bar.pop(0)
            print("The man now has",boss_bar,"health.")
        else:
            print("Scissors cuts paper! You lose.")
            player_health.pop(0)
            print("You now have",player_health,"health.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            boss_bar.pop(0)
            print("The man now has",boss_bar,"health.")
        else:
            print("Rock smashes scissors! You lose.")
            player_health.pop(0)
            print("You now have",player_health,"health.")

    if boss_bar == []:
        print("The man says: Congratulations, you have defeated me. You may now exit the game and escape.")
        time.sleep(1)
        print("But before you go please take this.\nThe mysterious man hands you a Collaboration star")
        starCount += 1
        collaborationStar()
        gameEnd()
        room3Start = False
    elif player_health == []:
        print(gameOver)
        print("You finished the game but didn't escape.")
        print("Your finished the game with a total of ",starCount,"Collaboration Stars\n Thanks for playing!")
        room3Start = False

    





    


