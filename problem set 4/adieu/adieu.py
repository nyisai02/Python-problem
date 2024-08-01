import inflect
p = inflect.engine()
mylist =["Adieu","adieu"]
while True:
    try:
        name=input("Name:")
        mylist.append(name)

    except:
        break
mylist[2]= "to " + mylist[2]
if len(mylist)==3:
    mm=p.join(mylist, conj="")
elif len(mylist)==4:
    mm=p.join(mylist, final_sep="")
else:
    mm=p.join(mylist)

print(mm)
