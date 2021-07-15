import random
import os
import time

colors='RGBY'
simon=""

for score in range(0,10):
    simon+=random.choice(colors) #Goes on adding 1 random color to list simon
    print(simon)
    for color in simon:
        print(color)
        time.sleep(1.5)
        os.system("cls")
    guess = input('Repeat:')
    os.system("cls")
    if guess != simon: #Checks whole list of input against simon
        break
print(f'Your score is {score}')

