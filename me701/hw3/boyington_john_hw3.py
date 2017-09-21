###############################################################################
#                            me701 hw3 (due: 9/22/17)
#                            john boyington
###############################################################################
# import statements
import numpy as np
import decimal as dec
import matplotlib.pyplot as plt

###############################################################################
#                               problem 1
###############################################################################

a = 'hello'
b = 'world'

c = a + ' ' + b

d = c.title()

e, f = d.split()

g = 123
h = 3.141592653589793
i = 6.022e23

j = '{}|{:6.4f}| {:4.2e}'.format(g, h, i)
print(j == '123|3.1416| 6.02e+23')  # check string is same as problem statement

j = 5
k = '..'.join([str(n) for n in range(j)])

###############################################################################
#                               problem 2
###############################################################################

# >>> a = [1, 2, 3]
# >>> b = a
# >>> a[0] = 99
# >>> a
# [99, 2, 3]
# >>> b
# [99, 2, 3]

# part 1
# This happens because in the statement b = a; b is not just assigned the same
# value as a, but actually points to the same location as a. So, whenever
# either is changed, the value they're pointing to changes and as a result, the
# other reflects that change, too.

# part 2

# method 1
# by using the copy module:
# import copy
# b = copy.copy(a)

# method 2
# by repeating the code used to create a to create b:
# b = [1, 2, 3]

###############################################################################
#                               problem 3
###############################################################################

# part 1
powers = [2 ** i for i in range(20)]

# part 2
points = [(i, j, k) for i in [1, 2, -1] for j in [8, 4, 3, 0] for k in [0, -1]]

# check to see if total number of elements is what is expected
print(len(points) == 3 * 4 * 2)

###############################################################################
#                               problem 4
###############################################################################


def decimal_to_binary(x, n):
    strX = str(x)
    left, right = strX[:strX.index('.')], strX[strX.index('.'):]

    # for the left side
    leftLength = len(left)
    leftTotal = 0
    leftBin = np.ones(leftLength)
    while leftTotal < int(left):
        leftTotal = np.array([e * (2**((ind + 1))) for ind, e in enumerate(leftBin[::-1])]).sum()
        leftBin = np.concatenate((np.array([1]), leftBin))
    finalLen = len(leftBin)

    leftBin = np.zeros(finalLen)

    for i in range(finalLen):
        leftBin[i] = 1
        summed = np.array([e * (2 ** (-(ind + 1) + finalLen)) for ind, e in enumerate(leftBin)]).sum()
        if summed > float(left):
            leftBin[i] = 0
    leftBinString = ''
    for e in leftBin.astype(int):
        leftBinString += '{}'.format(e)

    # for the right side of the decimal
    rightBin = np.zeros(n)
    for i in range(n):
        rightBin[i] = 1
        summed = np.array([e * (2**(-(ind + 1))) for ind, e in enumerate(rightBin)]).sum()
        if summed > float(right):
            rightBin[i] = 0
    rightBinString = ''
    for e in rightBin.astype(int):
        rightBinString += '{}'.format(e)
    return leftBinString + '.'+rightBinString


print(decimal_to_binary(123.625, 4) == '1111011.1010')


def binary_to_decimal(i, f):
    strI = str(i)
    left, right = np.array(list(strI[:strI.index('.')])).astype(float), np.array(list(strI[strI.index('.') + 1:])).astype(float)
    leftTot = np.array([e * (2 ** (-(ind + 1) + len(left))) for ind, e in enumerate(left)]).sum()
    rightTot = np.array([e * (2**(-(ind + 1))) for ind, e in enumerate(right)]).sum()
    return leftTot + rightTot

print(binary_to_decimal(1111011.1010, 4) == 123.625)


###############################################################################
#                               problem 5
###############################################################################

dec.getcontext().prec = 200


def option1(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s


def option2(a):
    s = 0
    a = sorted(a)
    for i in range(len(a)):
        s += a[i]
    return s


def option3(a):
    if len(a) <= 2:
        s = sum(a)
    else:
        s = option3(a[:len(a)//2]) + option3(a[len(a)//2:])
    return s


def optionDec(a):
    s = 0
    for i in range(len(a)):
        s += dec.Decimal('{:.200}'.format(a[i]))
    return s


n = 200
data = np.zeros((n, 5))
for i in range(n):
    a = np.random.rand(i + 1)

    best = '{:.50}'.format(optionDec(a))
    regSum = '{:.50}'.format(sum(a))
    data[i, 0] = dec.Decimal(best) - dec.Decimal(regSum)

    npSum = '{:.50}'.format(np.sum(a))
    data[i, 1] = dec.Decimal(best) - dec.Decimal(npSum)

    opt1 = '{:.50}'.format(option1(a))
    data[i, 2] = dec.Decimal(best) - dec.Decimal(opt1)

    opt2 = '{:.50}'.format(option2(a))
    data[i, 3] = dec.Decimal(best) - dec.Decimal(opt2)

    opt3 = '{:.50}'.format(option3(a))
    data[i, 4] = dec.Decimal(best) - dec.Decimal(opt3)


plt.figure(0)
plt.plot(np.arange(n) + 1, abs(data[:, 0]), label='Regular Sum')
plt.plot(np.arange(n) + 1, abs(data[:, 1]), label='Numpy Sum')
plt.plot(np.arange(n) + 1, abs((data[:, 2])), label='Option 1')
plt.plot(np.arange(n) + 1, abs((data[:, 3])), label='Option 2')
plt.plot(np.arange(n) + 1, abs((data[:, 4])), label='Option 3')
plt.xlabel('Number of Elements in Array')
plt.ylabel('Difference from Most Accurate')
plt.yscale('log')
plt.legend()
plt.savefig('errorComparison.png', dpi=400)

plt.figure(1)
plt.plot(np.arange(n) + 1, abs((data[:, 2])), label='Option 1')
plt.plot(np.arange(n) + 1, abs((data[:, 3])), label='Option 2')
plt.plot(np.arange(n) + 1, abs((data[:, 4])), label='Option 3')
plt.xlabel('Number of Elements in Array')
plt.ylabel('Difference from Most Accurate')
plt.yscale('log')
plt.legend()
plt.savefig('errorComparisonOptions.png', dpi=400)

plt.figure(2)
plt.plot(np.arange(n) + 1, abs(data[:, 0]), label='Regular Sum')
plt.plot(np.arange(n) + 1, abs(data[:, 1]), label='Numpy Sum')
plt.xlabel('Number of Elements in Array')
plt.ylabel('Difference from Most Accurate')
plt.yscale('log')
plt.legend()
plt.savefig('errorComparisonBuiltIns.png', dpi=400)

# check regular sum algorithm
check1 = True
check2 = True
check3 = True
check4 = True
check5 = True
check6 = True

for i in range(n):
    if not data[i, 0] == data[i, 2]:
        check1 = False
    if not data[i, 0] == data[i, 3]:
        check2 = False
    if not data[i, 0] == data[i, 4]:
        check3 = False
    if not data[i, 1] == data[i, 2]:
        check4 = False
    if not data[i, 1] == data[i, 3]:
        check5 = False
    if not data[i, 1] == data[i, 4]:
        check6 = False


print('Regular Sum is Identical to Option 1', check1)
print('Regular Sum is Identical to Option 2', check2)
print('Regular Sum is Identical to Option 3', check3)

print('Numpy Sum is Identical to Option 1', check4)
print('Numpy Sum is Identical to Option 2', check5)
print('Numpy Sum is Identical to Option 3', check6)
