# ne737 final project

import matplotlib.pyplot as plt
import numpy as np


def Extract(name):
    F = open('data/data0/{}.Spe'.format(name), 'r').readlines()
    for ii in range(len(F)):
        if '0 1023' in F[ii]:
            line = np.array(F[ii + 1:ii + 1025])
            data = np.loadtxt(line)
            return data
    return 


#creates lists that contain strings of all of the names of each detector and position
fd1n = []
for ii in (range(5)):
    for jj in (range(4)):
        fd1n.append('d1r{}c{}'.format(ii+1, jj+1))
fd2n = []
for ii in (range(5)):
    for jj in (range(4)):
        fd2n.append('d2r{}c{}'.format(ii+1, jj+1))
fd3n = []
for ii in (range(5)):
    for jj in (range(4)):
        fd3n.append('d3r{}c{}'.format(ii+1, jj+1))
        
ed1n = []
for ii in [1, 3, 5]:
    for jj in (range(4)):
        ed1n.append('D1ER{}C{}'.format(ii, jj+1))
ed2n = []
for ii in [1, 3, 5]:
    for jj in (range(4)):
        ed2n.append('D2ER{}C{}'.format(ii, jj+1))
ed3n = []
for ii in [1, 3, 5]:
    for jj in (range(4)):
        ed3n.append('D3ER{}C{}'.format(ii, jj+1))


#extracts the corresponding data from the file and then sums all of the counts within that file
fd1sum = []
for nn in fd1n:
    fd1sum.append(np.sum(Extract(nn)))
fd1sum = np.array(fd1sum).reshape(5,4)
fd2sum = []
for nn in fd2n:
    fd2sum.append(np.sum(Extract(nn)))
fd2sum = np.array(fd2sum).reshape(5,4)
fd3sum = []
for nn in fd3n:
    fd3sum.append(np.sum(Extract(nn)))
fd3sum = np.array(fd3sum).reshape(5,4)


ed1sum = []
for nn in ed1n:
    ed1sum.append(np.sum(Extract(nn)))
ed1sum = np.array(ed1sum).reshape(3,4)
ed2sum = []
for nn in ed2n:
    ed2sum.append(np.sum(Extract(nn)))
ed2sum = np.array(ed2sum).reshape(3,4)
ed3sum = []
for nn in ed3n:
    ed3sum.append(np.sum(Extract(nn)))
ed3sum = np.array(ed3sum).reshape(3,4)

print fd1sum
print fd2sum
print fd3sum
print ed1sum
print ed2sum
print ed3sum
#print np.sum(Extract('d1r4c3'))