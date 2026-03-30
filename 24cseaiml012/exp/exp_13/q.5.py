
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)
x,y=np.meshgrid(x,y)
z=np.sin(np.sqrt(x**2+y**2))
plt.contour(x,y,z,levels=10,cmap='viridis')
plt.title("contour plot")
plt.colorbar()
plt.show()