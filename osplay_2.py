import os
# Let's make sure we know which working directory we are in
cwd = os.getcwd()
print cwd, 'is the current working directory.'
 
# And which files are present in the cwd? Note that the '.' represents the current
# working directory
cwdfiles = os.listdir('.')
 
# The output of listdir is stored as a list, print item by item
for file in cwdfiles:
    print file



for file in cwdfiles:
    source_name = file
    link_name =  '%s.rn.fq' %(source_name)
    os.symlink(source_name, link_name)
    print file
    print source_name
    print link_name
    

