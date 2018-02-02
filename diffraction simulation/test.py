from matplotlib.pyplot import *
from numpy import *
from math import *
from mpl_toolkits.mplot3d import Axes3D

rc('text', usetex=True)

"timesteps"
dt = 100E-9
t0 = 0.0
t1 = 1E-6
N = 1 + ceil((t1-t0)/dt)
"constants"
m = 9.11E-31
e = -1.6E-19
E = [-1,-2,5]

"variables"
t  = linspace(t0, t1, N)
x = zeros(len(t))
y = zeros(len(t))
z = zeros(len(t))

vx = zeros(len(t))
vy = zeros(len(t))
vz = zeros(len(t))

ax = (e*E[0])/m
ay = (e*E[1])/m
az = (e*E[2])/m

"numerical solution"
for i in range(len(t)-1):
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt
    vz[i+1] = vz[i] + az*dt
    x[i+1] = x[i] + vx[i+1]*dt
    y[i+1] = y[i] + vy[i+1]*dt
    z[i+1] = z[i] + vz[i+1]*dt

fig = figure()
axes = fig.gca(projection='3d')
axes.plot(x,y,z)
show()