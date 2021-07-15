import random
number=random.randint(0,500)
found=False
tries=0
while not found:
    guess=int(input("Guess")) #input should be integer
    tries+=1
    if number==guess:
        found=True
        print(f"You found the {number} after{tries} tries")
    elif number>guess:
        print(f"number is greter then{guess}")
    else:
        print(f"number is less then{guess}")

