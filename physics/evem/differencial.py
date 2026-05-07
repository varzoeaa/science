import numpy as np
import matplotlib.pyplot as plt

# x(t) = x0 + v*t
x0 = 5
v = 2

t = np.linspace(0, 5, 100)
x = x0 + v * t

# Derivált (sebesség): dx/dt = v (állandó)
v_t = np.full_like(t, v)

fig, ax1 = plt.subplots(figsize=(8, 5))

# Hely-idő grafikon
ax1.plot(t, x, label=r"$x(t) = x_0 + vt$", color='b')
ax1.set_xlabel('t [s]')
ax1.set_ylabel('x [m]', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_title('Hely-idő grafikon és pillanatnyi sebesség')

# Érintő (sebesség) egy pontban
pont = 2  # t=2s
x_pont = x0 + v * pont
ax1.plot([pont-0.5, pont+0.5], [x0+v*(pont-0.5), x0+v*(pont+0.5)], 'g--', label='Érintő t=2s-nél')
ax1.scatter([pont], [x_pont], color='red', zorder=5)
ax1.legend(loc='upper left')

# Sebesség-idő grafikon (alsó tengelyen)
ax2 = ax1.twinx()
ax2.plot(t, v_t, 'r-', label=r"$v(t) = dx/dt = v$")
ax2.set_ylabel('v [m/s]', color='r')
ax2.tick_params(axis='y', labelcolor='r')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
