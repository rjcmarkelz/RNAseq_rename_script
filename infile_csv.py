
# import csv
# test_file = 'block_2_3_nocontaminants_play.csv'
# csv_file  = csv.DictReader(open(test_file, 'rU'), delimiter = ',', quotechar='"')

# for line in csv_file:
# 	print line

#http://stackoverflow.com/questions/15580425/os-symlink-vs-ln-s

#JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332_CR.fq


import csv
import os

# with open('block_2_3_nocontaminants_play.csv', 'rU') as f:
#     reader = csv.reader(f)
#     for row in reader:
#     	# print row[0]
#     	source_name = path/row[0].fq
#     	link_name = path/row[1].rn.fq
#     	os.symlink(source_name, link_name)
#     	# for i in row:
#     		# print i
#     	# print ' 1  2   3  '.split()
#         print row


with open('block_2_3_nocontaminants_play.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

data = dict()
with open('block_2_3_nocontaminants_play.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        old = row[0]
        new = row[1]
        data[old] = new
        print data
        #dictionary = dict(zip(key, value))
#print dictionary



# with open("block_2_3_nocontaminants_play.csv") as fd:
#     d = dict(line.rstrip().split(',', 1) for line in fd)
#     print d

# f = open("block_2_3_nocontaminants_play.csv", 'r')
# d = {}
# for line in f:
# 	print line
# 	k, v = line.strip().split(',', 1)
# 	d[k.strip()] = v.strip()
# f.close()
# print d

# d = dict((line.strip().split(',') for line in file("block_2_3_nocontaminants_play.csv")))






