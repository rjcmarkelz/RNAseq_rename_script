#!/usr/bin/python
import os 
import re
import csv
import sys

######################################################
######################################################
# Provide Pathnames for Target Folder and Symbolic
# Link Folder
######################################################
######################################################

block_num = sys.argv[1]
path = "/Users/Cody_2/git.repos/RILS/Block%s/project.maloof/" % (block_num)
path2 = "/Users/Cody_2/git.repos/RILS/Block%s/project.maloof.renamed/" % (block_num)

# path  = sys.argv[1]
# path2  = sys.argv[2]

#cody_1 path home imac
# path  = "/Users/Cody/Documents/Maloof Lab/My Brassica/Block2/project.maloof/"
# path2 = "/Users/Cody/Documents/Maloof Lab/My Brassica/Block2/project.maloof.rename/"

#cody_2 path laptop
# path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
# path2 = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof.renamed/"

# #user input
# path  = raw_input("Enter the absolute path for the input directory: ")
# print "------------------"
# print "You entered ", path
# print "------------------"
# print "------------------"

# path2 = raw_input("Now enter the absolute path for the directory containing the symbolic links: ")
# print "------------------"
# print "You entered ", path2
# print "------------------"
# print "------------------"

pathfiles = os.listdir(path)


###################################################
###################################################

#Small play dictionary for quick testing

RN_Dict = {
'RIL_360.02' :'RIL_1',
'RIL_73.02'  :'RIL_4',
'RIL_259.0' :'RIL_103(contaminated?)',
'RIL_251' :'RIL_IMB211',
'RIL_341' :'SIG_CON',
'RIL_265' :'RIL_113.rn',
}

# print RN_Dict
# keys   = RN_Dict.keys()
# values = RN_Dict.values()
# print keys
# print values
# RN_Dict = dict()

# with open('block_2_3_nocontaminants_play.csv', 'rU') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         old = row[0]
#         new = row[1]
#         RN_Dict[old] = new
#         print RN_Dict

re12 = '^RIL'
re13 = '_' 
re14 = '([A-Z0-9]+$)'
rg2 = re.compile(re12+re13+re14,re.IGNORECASE|re.DOTALL)

Uncon_Dict = {}
Con_Dict  = {}

for key in RN_Dict:
    match = rg2.search(RN_Dict[key])
    if match:
        Uncon_Dict[key] = RN_Dict[key]
        print "Uncontaminated: ", RN_Dict[key]
    else:
        Con_Dict[key] = RN_Dict[key]
        print "Contaminated: ", RN_Dict[key]
        
print Uncon_Dict
print Con_Dict
######################################################
######################################################

#text string examples
#'JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332_CR.fq'
#'JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_IMB211_CR.fq'
re1 = '.*?'     # Match frontend
re2 = '(Blk)'   # Blk
re3 = '(\\d+)'  # Blk_number
re4 = '(_)'     # underscore 
re5 = '(RIL)'   # RIL
re6 = '(_)'     # underscore 
re7 = '([A-Z0-9]+)'  # RIL_number
re8 = '(_)'                 # underscore
re9='((?:[a-z][a-z]+))'     # Treatment
re10='(.)'                  # dot (any character)
re11='((?:[a-z][a-z]+))'    # fq 

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11,re.IGNORECASE|re.DOTALL)

######################################################
######################################################

for fn in pathfiles:
    source_name = fn
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
        
        #remake block number to match dictionary key
        conv_Blk_num = '.' + str(Blk_number).zfill(2)
        print conv_Blk_num

        # capture = Blk + Blk_number + underscore1 + RIL + underscore2 + RIL_num + underscore3 + treatment + dot + fq
        # print capture

        oldname = RIL + underscore2 + RIL_num
        print oldname
        
        RIL_string = RIL + underscore2 + RIL_num + conv_Blk_num
        print RIL_string
        
        if RIL_string in Uncon_Dict:
            print "Making RIL name replacement. \n Old Name: %s; \n New Name: %s" % (oldname, Uncon_Dict[RIL_string])
            link_name = 'RN_' + source_name.replace(oldname, Uncon_Dict[RIL_string])
            print "Symbolic link will have name:", link_name
            symlinktarget = path  + "/" + source_name
            symlinkpath   = path2 + "/" + link_name
            print symlinktarget
            print symlinkpath
            os.symlink(symlinktarget, symlinkpath)
        else: 
            print "No it is not!"   
                
        print 
        print 
        print 

######################################################
######################################################



    








