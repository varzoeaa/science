import numpy as np
import matplotlib.pyplot as plt

# Példa paraméterek
x0 = 2   # kezdő hely [m]
v = 4    # sebesség [m/s]

# Időintervallum
T = 5  # másodperc
N = 100

t = np.linspace(0, T, N)
x = x0 + v * t

plt.figure(figsize=(8, 5))
plt.plot(t, x, label=fr"$x(t) = {x0} + {v}t$")

# Meredekség (sebesség) szemléltetése
plt.arrow(1, x0 + v*1, 1, v, head_width=0.15, head_length=0.5, fc='orange', ec='orange', label='Sebesség v')
plt.text(2.1, x0 + v*2 + 0.5, f"v = {v} m/s", color='orange')

# Nyugalom (v=0) példája
plt.hlines(x0, 0, T, colors='green', linestyles='dashed', label='v = 0 (nyugalom)')

# Negatív sebesség példája
v_neg = -3
x_neg = x0 + v_neg * t
plt.plot(t, x_neg, 'r--', label=fr"$x(t) = {x0} {v_neg:+}t$")

plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('Hely-idő grafikon: x(t) = x₀ + vt')
plt.legend()
plt.grid(True)
plt.show()
