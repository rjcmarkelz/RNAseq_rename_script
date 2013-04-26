import re

RN_Dict = {
'RIL_360.12' :'RIL_1(contaminated?)',
'RIL_73'  :'==',
'RIL_259' :'RIL_103(contaminated?)',
'RIL_251' :'RIL_IMB211',
'RIL_223' :'RIL_R500',
'RIL_251' :'RIL_4',
'RIL_113' :'(SIG_CON)',
'RIL_265' :'RIL_52/RIL_53',
'RIL_255' :'RIL_154.rn',
}

print RN_Dict
keys   = RN_Dict.keys()
values = RN_Dict.values()
print keys
print values

for k, v in RN_Dict.items():
    print ": ".join((k, v))

parenthesis = "("
plus = "+"
for keys in RN_Dict:
	if len(RN_Dict[keys]) > 7 and parenthesis in RN_Dict[keys]:
		print "These might be contaminated:", RN_Dict[keys]
	elif len(RN_Dict[keys]) > 7 and plus in RN_Dict[keys]:
	    print "These might be contaminated:", RN_Dict[keys]
	elif "==" in RN_Dict[keys]:
		print "These might be contaminated:", RN_Dict[keys]
	elif "/" in RN_Dict[keys]:
		print "These might be contaminated:", RN_Dict[keys]
	else :
		print RN_Dict[keys]

re12 = '^RIL'
re13 = '(_)' 
re14 = '([A-Z0-9]+$)'

rg2 = re.compile(re12+re13+re14,re.IGNORECASE|re.DOTALL)

for keys in RN_Dict:
	match = rg2.search(RN_Dict[keys])
	if match:
		print "Uncontaminted: ", RN_Dict[keys]
	else:
		print "Contaminated: ", RN_Dict[keys]
	    


