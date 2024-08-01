import csv
import sys
if (len(sys.argv)<3):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv)>3):
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
     sys.exit("Not a CSV file")
else:

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last" ,"house": "house"})
        try:
            with open(sys.argv[1],"r") as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                            x1,x2=row["name"].split(",")
                            house=row["house"]
                            writer.writerow({"first": x2.lstrip(), "last": x1 ,"house": house})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")