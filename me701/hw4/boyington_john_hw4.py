###############################################################################
#                                Homework 4
###############################################################################

import re

# TODO: comment everything


###############################################################################
#                                PROBLEM 1
###############################################################################


goodString = 'pit spot spate slap two respite '
badString = 'pt Pot peat part '
badList = badString.split()
goodList = goodString.split()[:3] + ['slap two'] + goodString.split()[-1:]

totString = goodString + badString

s = r'[a-z]*p[\s\S]t[a-z]*'
p = re.compile(s)
found = p.findall(totString)

print(sorted(found) == sorted(goodList))

###############################################################################
#                                PROBLEM 2
###############################################################################

with open('regex_sample_mcnp.txt', 'r') as f:
    mcnpOutput = f.read()

s = r'1tally'
tallyLocator = re.compile(s)
tallyIndx = tallyLocator.finditer(mcnpOutput)
indx = []
for match in tallyIndx:
    indx.append(match.span()[1])


s = r'\d.\d\d\d\dE[+-]\d\d   \d.\d\d\d\d\dE[+-]\d\d \d.\d\d\d\d'
dataPtrn = re.compile(s)

keys = [18, 28]
d = {keys[0]: {'energy': [], 'value': [], 'sigma': []}, keys[1]: {'energy': [], 'value': [], 'sigma': []}}
for i in range(len(keys)):
    data = dataPtrn.finditer(mcnpOutput[indx[i]:indx[i + 1]])
    for datum in data:
        dataStr = datum.group().split()
        d[keys[i]]['energy'].append(float(dataStr[0]))
        d[keys[i]]['value'].append(float(dataStr[1]))
        d[keys[i]]['sigma'].append(float(dataStr[2]))

checkDict = {18: {'energy': [0.0000E+00, 3.0000E-01, 2.0000E+02],
                  'value': [0.00000E+00, 0.00000E+00, 3.35200E-01],
                  'sigma': [0.0000, 0.0000, 0.0141]},
             28: {'energy': [0.0000E+00, 3.0000E-01, 2.0000E+02],
                  'value': [0.00000E+00, 7.00000E-04, 9.99300E-01],
                  'sigma': [0.0000, 0.3778, 0.0003]}}

print(d == checkDict)
