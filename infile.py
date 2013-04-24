
InFile = file('block_2_3_nocontaminants_play.txt', 'r')
content = InFile.read()
InFile.close()

print content
#only prints the last line from the file

#a = dict(open('block_2_3_nocontaminants_play.txt'))
#print a


# dict takes a sequence of  `(key, value)` pairs and turns in into a dict
#print dict(get_entries( infile ))

f = open('block_2_3_nocontaminants_play.txt')
for line in f:
	print line,
f.close()


with open('block_2_3_nocontaminants_play.txt', 'r') as f:
	
	for line in f:
		print line,

