#!/usr/bin/python
import os 

RN_Dict = {
'RIL_360' :'RIL_1.rn',
'RIL_73'  :'RIL_1.rn',
'RIL_259' :'RIL_103.rn',
'RIL_251' :'RIL_104.rn',
'RIL_113' :'RIL_113.rn',
'RIL_265' :'RIL_113.rn',
}
print RN_Dict

# Open a file
path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
pathfiles = os.listdir(path)

for file in pathfiles:
    source_name = file
    for key in RN_Dict:
        link_name = file.replace(key, RN_Dict[key])
        print link_name
        #os.symlink(source_name, link_name)
        #print file
        #print source_name
        #print link_name





