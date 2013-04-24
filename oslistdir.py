#http://stackoverflow.com/questions/5022777/
#batch-file-renaming-inserting-text-from-a-list-in-python-or-java

import os
path = "/Users/Cody_2/git.repos/RILS/Block1/project.maloof/"
f = open('list.txt', 'r')

for f in os.listdir( path ):
    try:
        os.rename(f, (f.name))