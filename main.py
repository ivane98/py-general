import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)

    next(csv_data)

    for l in csv_data:
        if l['FirstName'] == 'No Reward':
            break
        names.append(f"{l['FirstName']} {l['LastName']}")


html_output += f"<p>There are {len(names)} contributors</p>"

print(html_output)



