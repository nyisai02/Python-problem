date=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
        s = input("Date: ")

        if "/" in s:
            x, y, z = s.split("/")
        elif "," in s:
            s =s.replace(",","")
            x, y, z = s.split(" ")
            if x in date:
                x=date.index(x)+1
        else:
            continue
        try:
            if int(x)> 12 or int(y) > 31:
                continue
            else:
                break
        except ValueError:
              continue

print(f"{int(z)}-{int(x):02}-{int(y):02}")