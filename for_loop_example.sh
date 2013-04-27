for BLOCK in {1..12}
do
	./dict_os_regex_infile.py /Users/Cody_2/git.repos/RILS/Block$BLOCK/project.maloof/ /Users/Cody_2/git.repos/RILS/Block$BLOCK/project.maloof.renamed/
done


for BLOCK in {1..12}
do
	./dict_os_regex_infile.py $BLOCK
done


