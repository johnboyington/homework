###############################################################################
#                            me701 hw3 (due: 9/22/17)
#                            john boyington
###############################################################################
# import statements

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
#                               problem 3
###############################################################################


def decimal_to_binary(x, n):
    strX = str(x)
    left, right = strX[:strX.index('.')], strX[strX.index('.') + 1:]
    return left, right



print(decimal_to_binary(12345.85643, 10))








def binary_to_decimal(i, f):
    pass

