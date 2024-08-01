import random


def main():
     level = get_level()
     score = 0
     test  = 0
     questions = 0
     x,y= generate_integer(level)
     while questions < 10:
             try:
                 answer = input(f"{x} + {y} = ")
                 if int(answer) == int(x + y):
                   x,y= generate_integer(level)
                   score += 1
                   questions+=1
                 elif int(answer)!= int(x + y) and test != 2:
                   test += 1
                   print("EEE")
                 elif int(answer)!= int(x + y) and test == 2:
                      print("EEE")
                      print(f"{x} + {y} =",x + y)
                      x,y= generate_integer(level)
                      questions+=1
             except ValueError:
                 print("EEE")

     print ("Score:",score)

def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    for _ in range(10):
            if level == 1:
              x = random.randint(0,9)
              y = random.randint(0,9)
              return x,y
            elif level == 2:
              x = random.randint(10,99)
              y = random.randint(10,99)
              return x,y
            else:
                x = random.randint(100,999)
                y = random.randint(100,999)
                return x,y
if __name__ == "__main__":
    main()