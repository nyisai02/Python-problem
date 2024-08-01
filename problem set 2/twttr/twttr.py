vale= ["a","e","i","o","u"]
words=input("Input: ")

for letter in words:
    if not letter.lower() in vale:
        print(letter,end="")
print()

