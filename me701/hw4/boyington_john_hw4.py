###############################################################################
#                                Homework 4
###############################################################################

import re


###############################################################################
#                                PROBLEM 1
###############################################################################


goodString = 'pit spot spate slap two respite '
badString = 'pt Pot peat part '
badList = badString.split()
goodList = goodString.split()[:3] + ['slap two']  + goodString.split()[-1:]

totString = goodString + badString

expresso = r'p[a-z]+t'
found = re.findall(expresso, totString)

print(found == goodList)
print(found == badList)