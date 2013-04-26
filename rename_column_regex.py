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

re12 = '^RIL'
re13 = '(_)' 
re14 = '([A-Z0-9]+$)'
rg2 = re.compile(re12+re13+re14,re.IGNORECASE|re.DOTALL)

Uncon_Dict = {}
Con_Dict  = {}
for key in RN_Dict:
    match = rg2.search(RN_Dict[key])
    if match:
        Uncon_Dict[key] = RN_Dict[key]
        print "Uncontaminated: ", RN_Dict[key]
    else:
        Con_Dict[key] = RN_Dict[key]
        print "Contaminated: ", RN_Dict[key]
        
print Uncon_Dict
print Con_Dict

