def main():
    time=input("What time is it? ")
    n=convert(time)
    if n>=7 and n<=8:
        print("breakfast time")
    elif n>=12 and n<=13:
        print("lunch time")
    elif n>=18 and n<=19:
        print("dinner time")


def convert(time):
    h,m=time.split(":")
    h=float(h)+(float(m)/60)
    return h


if __name__ == "__main__":
    main()
