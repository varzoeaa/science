import numpy as np
import matplotlib.pyplot as plt

# x(t) = 10 - 3t
x0 = 10  # kezdő hely
v = -3  # sebesség

t = np.linspace(0, 5, 100)  # 0-tól 5 másodpercig
x = x0 + v * t

plt.figure(figsize=(8, 5))
plt.plot(t, x, label=r"$x(t) = 10 - 3t$")
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.axvline(0, color='gray', linestyle='--', linewidth=1)
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('Mozgás grafikonja: x(t) = 10 - 3t')
plt.legend()
plt.grid(True)
plt.show()
