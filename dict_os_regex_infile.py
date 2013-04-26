#!/usr/bin/python
import os 
import re
import csv



###################################################
###################################################

RN_Dict = dict()
with open('block_2_3_nocontaminants_play.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        old = row[0]
        new = row[1]
        RN_Dict[old] = new
        print RN_Dict

# RN_Dict = {
# 'RIL_360.12' :'RIL_1.rn',
# 'RIL_73'  :'RIL_4.rn',
# 'RIL_259' :'RIL_103.rn',
# 'RIL_251' :'RIL_104.rn',
# 'RIL_113' :'RIL_113.rn',
# 'RIL_265' :'RIL_113.rn',
# }

print RN_Dict
keys   = RN_Dict.keys()
values = RN_Dict.values()
print keys
print values



######################################################
######################################################
# Open a file
#cody_2 path laptop
#path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
#path2 = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof.renamed/"

#cody_1 path home imac
path  = "/Users/Cody/Documents/Maloof Lab/My Brassica/Block2/project.maloof/"
path2 = "/Users/Cody/Documents/Maloof Lab/My Brassica/Block2/project.maloof.rename/"

pathfiles = os.listdir(path)
######################################################
######################################################

#text string example
#txt = 'JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332676_CR.fq'
re1 = '.*?'     # Match frontend
re2 = '(Blk)'   # Blk
re3 = '(\\d+)'  # Blk_number
re4 = '(.)'     # underscore (any character)
re5 = '(RIL)'   # RIL
re6 = '(_)'     # underscore (any character)
re7 = '([A-Z0-9]+)'  # RIL_number
re8 = '(.)'                 # underscore (any character)
re9='((?:[a-z][a-z]+))'     # Treatment
re10='(.)'                  # dot (any character)
re11='((?:[a-z][a-z]+))'    # fq 

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11,re.IGNORECASE|re.DOTALL)
######################################################
######################################################

for file in pathfiles:
    source_name = file
    print source_name
    match = rg.search(source_name)
    if match:
        lead        = match.group(0)
        Blk         = match.group(1)
        Blk_number  = match.group(2)
        underscore1 = match.group(3)
        RIL         = match.group(4)
        underscore2 = match.group(5)
        RIL_num     = match.group(6)
        underscore3 = match.group(7)
        treatment   = match.group(8)
        dot         = match.group(9)
        fq          = match.group(10)

        conv_Blk_num = '.' + str(Blk_number).zfill(2)
        print conv_Blk_num

        capture = Blk + Blk_number + underscore1 + RIL + underscore2 + RIL_num + underscore3 + treatment + dot + fq
        print capture
        oldname = RIL + underscore2 + RIL_num
        print oldname
        RIL_string = RIL + underscore2 + RIL_num + conv_Blk_num
        print RIL_string
        
        if RIL_string in RN_Dict:
            print "Making RIL name replacement. \n Old Name: %s; \n New Name: %s" % (oldname, RN_Dict[RIL_string])
            link_name = source_name.replace(oldname, RN_Dict[RIL_string])
            print "Symbolic link will have name:", link_name
            symlinktarget = path  + source_name
            symlinkpath   = path2 + link_name
            print symlinktarget
            print symlinkpath
            os.symlink(symlinktarget, symlinkpath)
        else: 
            print "No it is not!"   
                
        print 
        print 
        print 





    








