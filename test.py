def box():
    print("As you kneel down to look at the big box you realize there is a 2 slot code lock. You have to find 2 numbers that will open the lock. Maybe something behind the door will give me the code.")
    testLock = input("Do you want to test the lock? type y for yes or n for no:")
    if testLock == "y":
        print("The lock has 2 slots that you can spin for numbers.")
        slot1 = input("What is the code for slot 1?:")
        if slot1 == "9":
            print("The lock clicked when you spun to 9, this mean you got the right answer!")
        else:
            print("The lock did not click when you spun to 9, this means it is not the right answer.")
        slot2 = input("What is the code for slot 2?")
        if slot2 == "6":
            print("The lock clicked when you spun to 6, this means you got the correct answer!")
        else:
            print("The lock did not click when you spun to 6, this means it is not the right answer.")
    if slot1 == "9" and slot2 == "6":
        boxOpen = True
        print("Good job you broke the code!\nNow you open the box and realize there is a hole at the bottom with a ladder.")


        
    room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")

def door1():
    print("You walking up to door 1 and it is open, you walk through and on the wall is a black board.\nOn the black board it says: Solve 2 + 15 -8")
    door1 = int(input("What is the answer to the question?:"))
    while door1 != 9:
        print("You write", door1, "on the black board and suddenly the board starts speaking\nThe blackboard says, Try again!")
        door1 = int(input("What is the answer to the question?:"))
    if door1 == 9:
         print("You write 9 on the black board and suddenly it starts speaking\nThe blackboard says, Good Job! Now LEAVE THIS ROOM! I NEED TO SLEEP! You quickly run out and close the door behind you.")
         room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")

def door2():
    print("You walk into door 2 and on the wall you find an old grandfather clock.\nYou notice that the minute hand is at 12, and the hour hand is at 6" )
    mixer.init()
    mixer.music.load('./Year9Game/music/clock.mp3')
    mixer.music.play()
    door2 = int(input("What time is it? (write the number, for example 2 not two) :"))
    while door2 != 6:
        print("You say",door2,"o clock out loud and suddenly the clock comes to life.\n Mr. Clock says: HEY THAT NOT MY CURRENT TIME, try again")
        door2 = int(input("What time is it?:"))
    if door2 == 6:
        print("You say 6 out loud and suddenly the clock comes to life.\nMr. Clock says: Nice, finally someone that can actually understand me, NOW SCRAM I NEED TO MOVE MY HANDS! \nSo you walk back out into the main room.")
        room1 = input("Where do you want to go? (Type 'B' for the box, '1' for door 1, '2' for door 2, '3' for door 3): ")
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