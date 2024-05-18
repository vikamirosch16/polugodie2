import csv
def yyy():
    with open("yyy.csv") as f:
        a=csv.reader(f)
        for row in a:
            print(row)
yyy()
