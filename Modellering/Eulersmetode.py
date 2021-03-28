from pylab import *

"Initialbetingelser"
a = 0
b = 100
dx = 1E-5
N = int((b-a)/dx)
y0 = 6000

"Matriser"
x = zeros(N+1)
y = zeros(N+1)

x[0] = 0
y[0] = y0


def Fder(y,x):
    return -30


"Eulers metode"
for n in range(N):
    y[n+1] = y[n] + Fder(y[n], x[n])*dx
    x[n+1] = x[n] + dx

print(x)
print(y)
    
plot(x,y)
show()