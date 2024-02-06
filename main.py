import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    next(csv_reader)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        
        for l in csv_reader:
            del l['email']
            csv_writer.writerow(l)