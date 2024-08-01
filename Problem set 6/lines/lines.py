import sys

def main():
    check_input()
    try:
        with open(sys.argv[1],"r")as file:
            count_line=0
            for line in file:
                if not line.lstrip().startswith("#") and not line.strip()=="":
                    count_line +=1
        print(count_line)
    except FileNotFoundError:
        sys.exit("File does not exit")


def check_input():
    if len(sys.argv)<2:
       sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

if __name__== '__main__':
    main()
