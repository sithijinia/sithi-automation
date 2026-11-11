import csv

try:
    with open("users.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["username"], row["password"])
except FileNotFoundError:
    print("Test data file not found!")
   