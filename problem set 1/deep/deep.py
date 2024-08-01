number = input("The number that you guess?  ")
if number.strip() == "42":
    print("Yes"," ")

elif number.lower() == "forty-two":
    print("Yes"," ")
elif number.lower() == "forty two":
    print("Yes"," ")
else:
    print("No")
