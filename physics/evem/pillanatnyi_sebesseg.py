import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Oda-vissza mozgás:
# A test 0 s-nál x = 0 m-ről indul,
# 5 s-nál eléri x = +5 m-t,
# 10 s-nál visszatér x = 0 m-be.
# -------------------------------------------------

# Időtengely
t = np.linspace(0, 10, 1000)

# Hely-idő függvény x(t)
# 0 <= t <= 5  esetén: x(t) = t
# 5 < t <= 10 esetén: x(t) = 10 - t
x = np.where(t <= 5, t, 10 - t)

# Derivált, vagyis pillanatnyi sebesség v(t)
# 0 <= t < 5  esetén: v(t) = +1 m/s
# 5 < t <= 10 esetén: v(t) = -1 m/s
# t = 5 s-nál matematikailag nem értelmezett a derivált
v = np.where(t < 5, 1, -1)

# A töréspont miatt a grafikonon kihagyjuk t = 5 környékét
v_gap = v.astype(float)
v_gap[np.abs(t - 5) < 0.03] = np.nan

# Átlagsebesség és átlagos elmozdulási sebesség
total_distance = 10
total_time = 10
displacement = 0

average_speed = total_distance / total_time
average_velocity = displacement / total_time

# -------------------------------------------------
# Ábra létrehozása
# -------------------------------------------------

fig, axes = plt.subplots(3, 1, figsize=(10, 10))

# -------------------------------------------------
# 1. Hely-idő grafikon
# -------------------------------------------------

axes[0].plot(t, x, linewidth=2)
axes[0].scatter([0, 5, 10], [0, 5, 0], zorder=3)

axes[0].set_title("Hely–idő függvény: x(t)")
axes[0].set_xlabel("Idő t [s]")
axes[0].set_ylabel("Helyzet x [m]")
axes[0].grid(True)

axes[0].annotate(
    "Indulás\nx = 0 m",
    xy=(0, 0),
    xytext=(0.7, 1),
    arrowprops=dict(arrowstyle="->")
)

axes[0].annotate(
    "Fordulópont\nitt töréspont van",
    xy=(5, 5),
    xytext=(5.7, 4),
    arrowprops=dict(arrowstyle="->")
)

axes[0].annotate(
    "Visszatérés\nx = 0 m",
    xy=(10, 0),
    xytext=(7.5, 1),
    arrowprops=dict(arrowstyle="->")
)

# -------------------------------------------------
# 2. A deriválás szemléltetése meredekséggel
# -------------------------------------------------

axes[1].plot(t, x, linewidth=2, label="x(t)")

# Érintő jellegű szakasz az első részen
tangent_t1 = np.array([1, 4])
tangent_x1 = tangent_t1
axes[1].plot(
    tangent_t1,
    tangent_x1,
    linestyle="--",
    linewidth=2,
    label="meredekség: dx/dt = +1 m/s"
)

# Érintő jellegű szakasz a második részen
tangent_t2 = np.array([6, 9])
tangent_x2 = 10 - tangent_t2
axes[1].plot(
    tangent_t2,
    tangent_x2,
    linestyle="--",
    linewidth=2,
    label="meredekség: dx/dt = -1 m/s"
)

axes[1].set_title("A deriválás grafikus jelentése: a meredekség adja a sebességet")
axes[1].set_xlabel("Idő t [s]")
axes[1].set_ylabel("Helyzet x [m]")
axes[1].grid(True)
axes[1].legend()

# -------------------------------------------------
# 3. Pillanatnyi sebesség grafikon
# -------------------------------------------------

axes[2].plot(t, v_gap, linewidth=2)

# Nyitott pont jelölése a nem értelmezett t = 5 s helyen
axes[2].scatter([5, 5], [1, -1], facecolors="none", edgecolors="black", zorder=3)

axes[2].axhline(0, linewidth=1)

axes[2].set_title("Pillanatnyi sebesség: v(t) = dx/dt")
axes[2].set_xlabel("Idő t [s]")
axes[2].set_ylabel("Sebesség v [m/s]")
axes[2].set_ylim(-1.5, 1.5)
axes[2].grid(True)

axes[2].annotate(
    "v = +1 m/s\npozitív irányú mozgás",
    xy=(2.5, 1),
    xytext=(1.2, 1.25),
    arrowprops=dict(arrowstyle="->")
)

axes[2].annotate(
    "v = -1 m/s\nnegatív irányú mozgás",
    xy=(7.5, -1),
    xytext=(6.3, -1.35),
    arrowprops=dict(arrowstyle="->")
)

axes[2].annotate(
    "t = 5 s-nál a derivált\nnem értelmezett",
    xy=(5, 0),
    xytext=(5.5, 0.35),
    arrowprops=dict(arrowstyle="->")
)

# -------------------------------------------------
# Képletmagyarázat az ábra alján
# -------------------------------------------------

result_text = (
    "Hely-idő függvény:\n"
    "0 ≤ t ≤ 5:   x(t) = t\n"
    "5 < t ≤ 10:  x(t) = 10 - t\n\n"
    "Derivált, vagyis pillanatnyi sebesség:\n"
    "0 ≤ t < 5:   v(t) = dx/dt = +1 m/s\n"
    "5 < t ≤ 10:  v(t) = dx/dt = -1 m/s\n"
    "t = 5 s-nál: a derivált nem értelmezett\n\n"
    f"Átlagsebesség: {average_speed:.1f} m/s | "
    f"Átlagos elmozdulási sebesség: {average_velocity:.1f} m/s"
)

fig.text(
    0.5,
    0.01,
    result_text,
    ha="center",
    va="bottom",
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black")
)

plt.tight_layout(rect=[0, 0.22, 1, 1])

# Mentés képként
plt.savefig("pillanatnyi_sebesseg_derivalt.png", dpi=300)

# Megjelenítés
plt.show()