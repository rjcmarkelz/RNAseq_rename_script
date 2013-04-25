#JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_332_CR.fq


/.+Blk(.+)\.fq$/

2_RIL_332_CR

id = [ 2, RIL, 332, CR ]

block = $id[0]
ril = $id[2]

if length block < 2, then $block = "0$block"

RIL_$ril.$block


