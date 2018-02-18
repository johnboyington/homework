'''
me777 hw2 problem 5, book problem 3.1
'''


def pm(x_i, a):
    return (a * x_i) % 13


def rng_chart(x_0):
    data = []
    for a in range(12):
        a += 1
        nums = [pm(x_0, a)]
        for i in range(12):
            x_new = pm(nums[-1], a)
            if x_new in nums:
                break
            nums.append(x_new)
        nums = [a, x_0] + nums
        data.append(nums)

    s = '  a  x_0    1    2    3    4    5    6    7    8    9   10   11   12\n'
    s += '--------------------------------------------------------------------\n'

    for d in data:
        for i in d:
            s += '{:3}  '.format(i)
        s += '\n'
    return s


for i in [1, 2, 3, 6, 9]:
    p = rng_chart(i)
    print(p)
