friend1Name = "a"
a = False
incorrectScore = 0
riddleAnswer = input("What is the answer to the question?:")
while a == False:
    if "age" in riddleAnswer:
            print("The whiteboard says: Almost there, think a little deeper!")
            riddleAnswer = input("What is the answer to the question?:")
            incorrectScore += 1
    elif riddleAnswer == "a":
        incorrectScore = 0
        print(friend1Name,"says: Good job! We did it")
        a = True
    else:
        print("The whiteboard says: Not quite, please try again!")
        riddleAnswer = input("What is the answer to the question?:")
        incorrectScore += 1
    if incorrectScore == 1:
        print(friend1Name, "says: OH I think I have heard of this riddle before. I think the answer is your age. Your age always goes up but never comes down!")
    elif incorrectScore == 3:
        print(friend1Name, "says: WOW now it makes sense to me, think about the first few question when we first started this game.")