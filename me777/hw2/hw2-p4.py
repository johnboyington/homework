'''
me777 hw2 problem 4
'''


def pm(x_i, a, m):
    return (a * x_i) % m


a = 16807
m = (2**31) - 1
x_0 = 1

x_n = x_0
i = 1
while i < 10002:
    x_n = pm(x_n, a, m)
    i += 1

print('x_{} = {}'.format(i, x_n))
