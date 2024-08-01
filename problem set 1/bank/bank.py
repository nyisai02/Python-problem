Greet=input("HEllO >>> ").lower().strip()

if Greet.startswith("hello"):
    print("$0")
elif Greet.startswith("h"):
    print("$20")
else :
    print("$100")