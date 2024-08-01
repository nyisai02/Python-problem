def main():
    num = input('Fraction: ')
    g=convert(num)
    n=gauge(g)
    print(n)


def convert(num):
    while True:
        try:
            if "/" in num:
                x,y=num.split("/")
                x=int(x)
                y=int(y)

            if x==1 and y==0:
                raise ZeroDivisionError

            if x>y:
                num = input('Fraction: ')
                continue
            else:
                g=round((x/y)*100)
                return g

        except ValueError:
            raise
        except ZeroDivisionError:
            raise



def gauge(g):
        if 99 <= g :
            return "F"
        elif g <= 1:
            return "E"

        else:
            return str(g)+"%"


if __name__ == "__main__":
    main()



