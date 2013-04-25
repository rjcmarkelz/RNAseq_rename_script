import re

#text string example
txt = 'JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332676_CR.fq'

re1 = '.*?'	    # Match frontend
re2 = '(Blk)'	# Blk
re3 = '(\\d)'  	# Blk_number
re4 = '(.)'	    # underscore (any character)
re5 = '(RIL)'	# RIL
re6 = '(_)'	    # underscore (any character)
re7 = '(\\d+)'	# RIL_number
re8 = '(.)'	    # underscore (any character)
rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8 ,re.IGNORECASE|re.DOTALL)


match = rg.search(txt)
if match:
    Blk         = match.group(1)
    Blk_number  = match.group(2)
    underscore1 = match.group(3)
    RIL         = match.group(4)
    underscore2 = match.group(5)
    RIL_num     = match.group(6)
    underscore3 = match.group(7)

    capture = Blk + Blk_number + underscore1 + RIL + underscore2 + RIL_num + underscore3 
    RIL_string = RIL + underscore2 + RIL_num
    print capture
    print RIL_string

