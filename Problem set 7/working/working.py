import re
def main():
    print(convert(input("Hours: ")))
def convert(s):
    lis = []
    time = ""
    input = re.search(r"(\d*)(:[0-5][0-9])*\s*(AM|PM)\s?(to)\s?(\d*)(:[0-5][0-9])*\s*(AM|PM)",s)


    try:
        for r in input.groups():
            if r == None:
                lis.append(":00")
            else:
                lis.append(r)

        if lis[2] == "PM"  and int(lis [0]) < 12:
                    lis[0] = str(int(lis[0]) + 12)

        if lis[6]=="PM" and int(lis[4]) < 12:
                    lis[4] = str(int(lis[4]) + 12)
        for j in [0, 4]:
            if int(lis[j]) == 12 :
                if lis[j+2] == "AM":
                        lis[j] = "00"
            lis[j] = f"{int(lis[j]):02d}"

        time += lis[0]
        for i in lis[1:]:
            if i != "PM" and i != "AM":
                if ":" not in i:
                    time += " "
                time += i

    except:
        raise ValueError
    return time
if __name__ == "__main__":

    main()





