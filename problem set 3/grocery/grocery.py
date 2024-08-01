d={}
while True:

    try:
        item = input()
        if item in d:
           d[item]+=1
        else:
            d[item]=1
    except EOFError:
        for i in sorted(d.keys()):
            key = i.upper()
            value = d[i]
            print(f"{value} {key}")
        break
