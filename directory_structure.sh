
#bash commands to copy directory structure from one 
#place into another without files

cd /path/to/directories &&
find . -type d -exec mkdir -p -- /path/to/backup/{} \;

ln -s /Users/Cody_2/git.repos/RILS/Block1/project.maloof/
project.maloof.link

ln -s -f /Users/Cody_2/git.repos/RILS/Block1/project.maloof/RIL_2.fq
  /Users/Cody_2/git.repos/RILS_2/Block1/project.maloof/RIL_2_new.fq
