#!/usr/bin/python
import os 
import re

#text string example
#txt = 'JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332676_CR.fq'
re1 = '.*?'	    # Match frontend
re2 = '(Blk)'	# Blk
re3 = '(\\d)'  	# Blk_number
re4 = '(.)'	    # underscore (any character)
re5 = '(RIL)'	# RIL
re6 = '(_)'	    # underscore (any character)
re7 = '(\\d+)'	# RIL_number
re8 = '(.)'	                # underscore (any character)
re9='((?:[a-z][a-z]+))'  	# Treatment
re10='(.)'	                # dot (any character)
re11='((?:[a-z][a-z]+))'	# fq 

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11,re.IGNORECASE|re.DOTALL)


RN_Dict = {
'RIL_360' :'RIL_1.rn',
'RIL_73'  :'RIL_4.rn',
'RIL_259' :'RIL_103.rn',
'RIL_251' :'RIL_104.rn',
'RIL_113' :'RIL_113.rn',
'RIL_265' :'RIL_113.rn',
}

print RN_Dict
keys   = RN_Dict.keys()
values = RN_Dict.values()
print keys
print values

# Open a file
#cody_2 path laptop
#path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
#path2 = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof.renamed/"

#cody_1 path home imac
path = "/Users/Cody/Documents/Maloof Lab/My Brassica/Block2/project.maloof/"
path2= "/Users/Cody/Documents/Maloof Lab/My Brassica/Block2/project.maloof.rename/"

pathfiles = os.listdir(path)

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

        capture = Blk + Blk_number + underscore1 + RIL + underscore2 + RIL_num + underscore3 + treatment + dot + fq
        RIL_string = RIL + underscore2 + RIL_num
        print capture
        print RIL_string
        
        if RIL_string in RN_Dict:
            print "Making RIL name replacement. Old Name: %s; New Name: %s" % (RIL_string, RN_Dict[RIL_string])
            link_name_y = source_name.replace(RIL_string, RN_Dict[RIL_string])
            print link_name_y
            symlinktarget = path  + source_name
            symlinkpath   = path2 + link_name_y
            print symlinktarget
            print symlinkpath
            #os.symlink(symlinktarget, symlinkpath)
        else: 
            print "No it is not!"   
                
        print 
        print 
        print 





    








