def main():
    new_text=input("Input: ")
    m=shorten(new_text)
    print(m)


def shorten(words):
    i=""
    for letter in words:
        if not letter.lower() in ["a","e","i","o","u"]:
            i+=letter
    return i

if __name__ == "__main__":
    main()
