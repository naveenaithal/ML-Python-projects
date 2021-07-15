import random
player=0
cpu=0
print("three  poin win the game!")
while cpu<3 and player<3:
    cpu_choice=random.choice(['rock','paper','scissors'])
    player_choice=input("Rock,paper and scissors")

    print(f"player choice {player_choice}, cpu choice {cpu_choice}")
    if player_choice.lower()==cpu_choice:
           print("Tie no one got points")
    elif player_choice=='paper':
        if cpu_choice=='rock':
            player+=1
        elif cpu_choice=='scissors':
            cpu+=1
    elif player_choice=='rock':
        if cpu_choice=='scissor':
            player+=1
        elif cpu_choice=='paper':
            cpu+=1
    elif player_choice=='scissors':
        if cpu_choice=='paper':
            player+=1
        elif cpu_choice=='rock':
            cpu+=1
    else:
        print('invalid input')


print(f"player has got {player} points,cpu has got {cpu}points")

