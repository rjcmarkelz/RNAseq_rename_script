import csv

data = dict()
with open('block_2_3_nocontaminants_play.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        old = row[0]
        new = row[1]
        data[old] = new
        print data







