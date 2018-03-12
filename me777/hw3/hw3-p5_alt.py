from numpy.random import rand
import numpy as np
import matplotlib.pyplot as plt

sampsize=[10,100,1000,10000,100000,1000000]#,10000000,100000000] # Sample Sizes
sampsize=np.logspace(2, 6, 20).astype(int)

b=3 # Upper Bound

a=1 # Lower Bound

summ=0 # Sum of the data set at zero

summ2=0 # second sum for antithetic variates

err1=[] # error list

err2=[] # error list

fbarsq = 0 # fbar^2

fsqbar = 0 # f^2 bar

ans1=[] # answer list

ans2=[] # answer list

stddev1= [] # list for standard deviation

stddev2 =[] # list for standard deviation

true=48.4 # True value for the integral

for i in range(1,sampsize[-1]+1): # for loop for largest sample size

    r=rand() # random number

    x=1+r*2 # define x to be in the bounds

    x2=1+(1-r)*2 # a second x for antithetic variates

    summ+=x**4 # Simple sample mean method

    summ2+=x2**4 # Antithetic variates method wtih new x

    fbarsq+=x**4 # parameter for standard deviation in sample mean method

    fsqbar+=(x**4)**2 # 2nd parameter for standard deviation in sample mean method

    if i in sampsize: # When sample size reached append data

        ans1.append((b-a)/i*summ) # Sample mean method

        ans2.append((b-a)/i*(summ+summ2)/2) # Antithetic variates method

        err1.append(abs(((b-a)/i*summ)-true)*100/true) # Samle mean variates% error

        err2.append(abs(((b-a)/i*(summ+summ2)/2-true)*100/true)) # Antithetic variates % error

        stddev1.append(((((fbarsq/i)**2 + (fsqbar/i))*i/(i-1))/i)**0.5)

        stddev2.append(((1/i)*(1/2*summ/i*summ2/i+((summ/i)**2 - (1/(2*i)*(summ + summ2))**2)))*0.5)

plt.figure(0)
plt.plot(sampsize, ans1, 'k', label='Sample Mean')
plt.plot(sampsize, ans2, 'g:', label='Antithetical')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('I')
plt.legend()

plt.figure(1)
plt.plot(sampsize, err1, 'k', label='Sample Mean')
plt.plot(sampsize, err2, 'g:', label='Antithetical')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()

plt.figure(2)
plt.plot(sampsize, stddev1, 'k', label='Sample Mean')
plt.plot(sampsize, stddev2, 'g:', label='Antithetical')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('$\sigma$')
plt.legend()
