import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi,100)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y = cos(x)')
plt.grid()
plt.savefig('grafica.png')