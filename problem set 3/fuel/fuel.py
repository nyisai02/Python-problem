while True:
    try:
        num = input('Fraction: ')
        if "/" in num:
            x,y=num.split("/")
            x=int(x)
            y=int(y)
            g=round((x/y)*100)
            if x>y:
               continue
            

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
if 99 <= g :
    print("F")
elif g <= 1:
    print("E")
else:
    print(f"{str(g)}"+"%")
