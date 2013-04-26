RN_Dict = {
'RIL_360.12' :'RIL_1(contaminated?)',
'RIL_73'  :'RIL_4',
'RIL_259' :'RIL_103(contaminated?)',
'RIL_251' :'RIL_IMB211',
'RIL_113' :'(SIG_CON)',
'RIL_265' :'RIL_113.rn',
'RIL_255' :'RIL_154.rn',
}

print RN_Dict
keys   = RN_Dict.keys()
values = RN_Dict.values()
print keys
print values

parenthesis = "("
for keys in RN_Dict:
	if len(RN_Dict[keys]) > 7 and parenthesis in RN_Dict[keys]:
		print "These might be contaminated:", RN_Dict[keys]
	else:
	    print RN_Dict[keys]