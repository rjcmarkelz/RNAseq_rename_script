

d = {}
with open("block_2_3_nocontaminants.txt", 'r') as f:
	for line in f:
		tmp = line.strip().split('	')
		d[tmp[0]] = tuple(tmp[1],tmp[2])

    