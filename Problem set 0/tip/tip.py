def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dpp=d.replace("$","")
    return float(dpp)


def percent_to_float(p):
    ppd=p.replace("%","")
    pd=float(ppd)/100
    return pd

main()
