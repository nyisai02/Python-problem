import sys
import csv

from tabulate import tabulate

list = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1],"r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(tabulate(list, headers="keys", tablefmt="grid"))