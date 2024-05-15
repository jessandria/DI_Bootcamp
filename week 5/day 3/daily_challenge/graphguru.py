import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(0, 20, 100)


y = x ** 2


plt.plot(x, y)


plt.title('Plot of x vs x^2')
plt.xlabel('x')
plt.ylabel('x^2')

plt.xlim(0, 20)
plt.ylim(0, 400)  

plt.savefig('x_vs_x_squared.png')

plt.show()
