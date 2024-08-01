n=input("camelCase: ")

for c in n:
    if c.isupper():
         print("_"+c.lower(),end="")
    else:
        print(c,end="")

print()
