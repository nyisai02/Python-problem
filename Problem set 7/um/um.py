import re
def main():
    print(count(input("Text: ")))

def count(s):
    um =r"\bum\b"
    count = re.findall(um,s,re.IGNORECASE)
    return len(count)

if __name__ == "__main__":
    main()