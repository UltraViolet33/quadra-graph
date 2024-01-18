import numpy as np
import matplotlib.pyplot as plt
import sys

print('QUADRATIC GRAPH')
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
except IndexError:
    print("Missing values - Usage: python quadra.py a b c")
    sys.exit()



x = np.linspace(-500, 500, 500)

y = a * x**2 + b * x + c

plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Equation Visualization')
plt.legend()

plt.show()