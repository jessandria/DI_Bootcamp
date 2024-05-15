import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 10, 20)
y1 = x ** 2
y2 = x ** 1.5

#Create a line plot of y1 against x.
#Create a scatter plot of y2 against x.

fig, ax= plt.subplots()
ax.plot(x,y1)
ax.scatter(x,y2)

plt.show()
#fig.savefig("Basicplot.png")