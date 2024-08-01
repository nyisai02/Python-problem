import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
desi=figlet.getFonts()

if len(sys.argv) ==1:
    figlet.setFont(font=random.choice(desi))

elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")
word=input("Input: ")
print("Out put: "+figlet.renderText(word))









