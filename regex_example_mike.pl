#!/usr/bin/python
import os 
import re

#Example file name
file_name = "JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332_CR.fq";

#Regex to match what I want
capture = re.search(r'/.+Blk(.+)\.fq$/', file_name, flags = 0)
print capture


#2_RIL_332_CR
# capture = re.compile(r'_')
# id = capture.split(filename, 1) #where filename is CHEESE_CHEESE_TYPE.***

#id = [ 2, RIL, 332, CR ]

#block = id[0]
#ril = id[2]

#if length block < 2, then $block = "0$block"

#RIL_$ril.$block


# RN_Dict = {
# 'RIL_360' :'RIL_1.rn',
# 'RIL_73'  :'RIL_1.rn',
# 'RIL_259' :'RIL_103.rn',
# 'RIL_251' :'RIL_104.rn',
# 'RIL_113' :'RIL_113.rn',
# 'RIL_265' :'RIL_113.rn',
# }
# print RN_Dict

# # Open a file
# path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
# pathfiles = os.listdir(path)

# for file in pathfiles:
#     source_name = file
#     for key in RN_Dict:
#         link_name = file.replace(key, RN_Dict[key])
#         print link_name
#         #os.symlink(source_name, link_name)
#         #print file
#         #print source_name
#         #print link_name


###renamer
###research re, glob, os  module documentation
# glob---- http://docs.python.org/2/library/glob.html#module-glob
# re------ http://docs.python.org/2/library/re.html
# # os------ http://docs.python.org/2/library/os.html#module-os
# import re, glob, os

# def renamer(files, pattern, replacement):
#     for pathname in glob.glob(files):
#         basename= os.path.basename(pathname)
#         new_filename= re.sub(pattern, replacement, basename)
#         if new_filename != basename:
#             os.rename(
#               pathname,
#               os.path.join(os.path.dirname(pathname), new_filename))

# renamer("*.doc", r"^(.*)\.doc$", r"new(\1).doc")





