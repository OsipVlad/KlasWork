import csv



columns = [
    "id",
    "login",
    "password",
    "role",
]

with open("db.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(columns)
    csvwriter.writerows()
