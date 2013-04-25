#!/usr/bin/python

import os, sys


path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
dirs = os.listdir( path )
# This would print all the files and directories
for file in dirs:
    print file

# Open a file
filelist =open('filelist.txt', 'w')

path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
dirs = os.listdir( path )
print dirs
# This would print all the files and directories
for file in dirs:
    print file






###renamer
###research re, glob, os  module documentation
# glob---- http://docs.python.org/2/library/glob.html#module-glob
# re------ http://docs.python.org/2/library/re.html
# os------ http://docs.python.org/2/library/os.html#module-os
import re, glob, os

def renamer(files, pattern, replacement):
    for pathname in glob.glob(files):
        basename= os.path.basename(pathname)
        new_filename= re.sub(pattern, replacement, basename)
        if new_filename != basename:
            os.rename(
              pathname,
              os.path.join(os.path.dirname(pathname), new_filename))

renamer("*.doc", r"^(.*)\.doc$", r"new(\1).doc")


import re
p = re.compile(r'_')
p.split(filename, 1) #where filename is CHEESE_CHEESE_TYPE.***