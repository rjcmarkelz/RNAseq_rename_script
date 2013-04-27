RN_Dict = {
'RIL_360' :'RIL_1.rn',
'RIL_73'  :'RIL_1.rn',
'RIL_259' :'RIL_103.rn',
'RIL_251' :'RIL_104.rn',
'RIL_113' :'RIL_113.rn',
'RIL_265' :'RIL_113.rn',
}

text = """
    JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_360_CR.fq
    JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_337_CR.fq
    JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_339_CR.fq
    JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_73_CR.fq
    JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_341_CR.fq
    JD002_6_NoIndex_L005_R1_all.fastq.gz.Blk2_RIL_265_CR.fq
    """

print RN_Dict

for key in RN_Dict:
    text_2 = text.replace(key, RN_Dict[key])
    #print text
    print text_2