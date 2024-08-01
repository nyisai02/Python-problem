import random
while True:
    try:
        level=int(input("level: "))
        if level >0:
            break
    except ValueError:
        pass
e=random.randint(1,level)

while True:


    try:
        n=int(input("Guess: "))
        if n>=1:
            if e<n:
                print("Too large!")
            elif e>n:
                print("Too small!")
            else:
                print("Just right!")
                break

    except ValueError:
        pass




