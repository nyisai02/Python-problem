def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s)<2 or len(s)>6:
      return False
    if s[0].isdigit() or s[1].isdigit():
      return False

    i=0
    while i < len(s):
        if not s[i].isalpha()==True:
            if s[i]=="0":
                return False
            else :
                break
        i+=1

    for exter in s:
        if not exter.isalnum():
           return False

    return True

main()
