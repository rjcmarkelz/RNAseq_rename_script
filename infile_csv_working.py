import csv

data = dict()
with open('entire_rename_list.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        old = row[0]
        new = row[1]
        data[old] = new
        #print data


length = len(data)
print length #1022



