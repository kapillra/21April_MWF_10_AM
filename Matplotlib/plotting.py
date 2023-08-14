# importing libs
import numpy as np
import matplotlib.pyplot as plt

x = [*range(1,8)]
y = [np.random.randint(10, 99) for i in range(1, 8)]

plt.xlabel("Days")
plt.ylabel('Temperature')
plt.title("Weather")
plt.plot(x, y, color='blue', linewidth=2, linestyle='dotted')

plt.show()