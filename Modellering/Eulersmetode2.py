g = 9.8         # m/s**2
v = 1           # m/s
dt = 1E-8       # s
tid_slutt = 10  # s
t = 0           # Starttid
m = 1           # Kg
k = 0.1         # Luftmotstand

while t < tid_slutt:
    a = g
    v = v + a*dt #Eulers metode
    t = t + dt
    
print("Sluttfarten er", v)