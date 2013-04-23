#!/usr/bin/python
#Renaming Script v0.1
#2013_04_19

#problem
#import the list of old/new file names
#input from user the directory where the files are
#input from user where the directory of results is to go
#read all of the file names in from the file directory
#search each file name for _RIL_XXX
#compare this against the list of old/new names
#rename the variables based on the list
#create symbolic links with the new names to the old file names
#append a .rn.fq 









#!/usr/bin/python
import os, sys

# Open a file
path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
dirs = os.listdir( path )

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


