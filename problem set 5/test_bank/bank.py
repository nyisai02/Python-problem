def main():
    Greet=input("HEllO >>> ")
    m=value(Greet)
    print("$"+value)


def value(Greeting):
        Greeting=Greeting.lower().strip()
        if Greeting.startswith("hello"):
                return 0
        elif Greeting.startswith("h"):
                return 20
        else :
                return 100


if __name__ == "__main__":
    main()
