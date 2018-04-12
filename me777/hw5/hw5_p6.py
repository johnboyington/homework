import numpy as np

import matplotlib.pyplot as plt

from numpy.random import rand

from numpy.linalg import norm

 

# This section defines the polygon

 

N= int(round(np.random.uniform(3,20),0))      # Pick random N bewteen 3 and 20

r= 1.0                          # Interior radius

D=r/np.cos(np.pi/N)             # Radius of vertices

x=np.zeros(N)

y=np.zeros(N)

for i in range(N):

    x[i]= D*(np.cos(2*np.pi*i/float(N)))

    y[i]= D*(np.sin(2*np.pi*i/float(N)))

x=np.append(x,x[0])

y=np.append(y,y[0])

ax = plt.gca()

ax.cla()

for i in range(0, len(x), 1):

    ax.plot(x[i:i+2], y[i:i+2], 'r-')

    #print x[i:i+2], y[i:i+2]\

 

#This section defines the circle origin

x_0 = r*rand()-(r/2)

y_0 = r*rand()-(r/2)

 

#This section determines the maximal circle radius

sect = np.zeros(N)

for i in range(N):

    sect[i] = 2*np.pi*i/float(N)

   

# Determine theta of x_0 and y_0 from origin

if x_0 >0 and y_0 > 0:

    theta_2 = np.arctan(y_0/x_0)

elif x_0 < 0 and y_0 > 0:

    theta_2 = np.pi + np.arctan(y_0/x_0)

elif x_0 < 0 and y_0 < 0:

    theta_2 = np.pi + np.arctan(y_0/x_0)

else:

    theta_2 = 2*np.pi + np.arctan(y_0/x_0)

   

#This section finds the sector in which the circle origin resides

zone = 0

for i in range(N-1):

    if theta_2 > sect[i] and theta_2 < sect[i+1]:

        zone = i

    elif theta_2 > sect[N-1]:

        zone = N-1

       

# This section computes the distance to the side of polygon

x_z1,y_z1,x_z2,y_z2 = x[zone],y[zone],x[zone+1],y[zone+1]

p1,p2,p3 = np.array([x_z1,y_z1]),np.array([x_z2,y_z2]),np.array([x_0,y_0])

R = norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)

AB = p2-p1

AP = p3-p1

 

 

# This section finds the point where the circle and polygon touch

k =p1 + np.dot(AP,AB)/np.dot(AB,AB) * AB

 

#This section plots the circle

circle = plt.Circle((x_0, y_0), R, color='b', fill=False)

ax.add_artist(circle)

ax.plot(x_0,y_0,'ko')

ax.plot(k[0],k[1],'ko')

ax.set_xlim(-(1.5*r),(1.5*r))

ax.set_ylim(-(1.5*r),(1.5*r))

ax.set_xlabel('x')

ax.set_ylabel('y')

title = "inscribed circl with " + str(N) + " sides"

ax.set_title(title)

print("(x,y): (" + str(x_0) + "," + str(y_0) + ")")

print("Radius: " + str(R))