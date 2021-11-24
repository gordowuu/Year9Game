from pygame import mixer
import time

mixer.init() #Initialzing pyamge mixer
mixer.music.load('frogSounds.mp3') #Loading Music File

#Timer based
mixer.music.play() #Playing Music with Pygame
time.sleep(5)
mixer.music.stop()

#not part of the example, just here to separate the two sections
time.sleep(3)

#While waiting for user input
#Your user input loop will be whatever you need it to be.
#The point is to start the music before the loop and stop it after

mixer.music.play()
answer = input("Enter y ")
while 'y' not in answer:
    print ("Sorry, incorrect")
    answer = input('Enter y ')
mixer.music.stop()