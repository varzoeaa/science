import matplotlib.pyplot as plt
import numpy as np

# Időpontok másodpercben
# 0 s: indulás az origóból
# 5 s: eléri a +5 m pontot
# 10 s: visszatér az origóba
time = np.array([0, 5, 10])

# Helyzet az x tengelyen méterben
position = np.array([0, 5, 0])

# Megtett út idő szerint
# 0 s-nál: 0 m
# 5 s-nál: 5 m
# 10 s-nál: 10 m
distance = np.array([0, 5, 10])

# Fizikai mennyiségek
total_distance = distance[-1]
total_time = time[-1] - time[0]
displacement = position[-1] - position[0]

average_speed = total_distance / total_time
average_velocity = displacement / total_time

# Ábra létrehozása
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# -------------------------------------------------
# 1. grafikon: helyzet-idő grafikon
# -------------------------------------------------
axes[0].plot(time, position, marker="o", linewidth=2)

axes[0].set_title("Helyzet–idő grafikon: oda-vissza mozgás")
axes[0].set_xlabel("Idő [t]")
axes[0].set_ylabel("Helyzet x [m]")
axes[0].grid(True)

axes[0].annotate(
    "Indulás\nx = 0 m",
    xy=(0, 0),
    xytext=(0.5, 1),
    arrowprops=dict(arrowstyle="->")
)

axes[0].annotate(
    "Fordulópont\nx = +5 m",
    xy=(5, 5),
    xytext=(5.5, 4),
    arrowprops=dict(arrowstyle="->")
)

axes[0].annotate(
    "Visszatérés\nx = 0 m",
    xy=(10, 0),
    xytext=(7.5, 1),
    arrowprops=dict(arrowstyle="->")
)

# -------------------------------------------------
# 2. grafikon: megtett út-idő grafikon
# -------------------------------------------------
axes[1].plot(time, distance, marker="o", linewidth=2)

axes[1].set_title("Megtett út–idő grafikon")
axes[1].set_xlabel("Idő [t]")
axes[1].set_ylabel("Megtett út s [m]")
axes[1].grid(True)

# Átlagsebesség vonalának jelölése
axes[1].plot(
    [time[0], time[-1]],
    [distance[0], distance[-1]],
    linestyle="--",
    linewidth=2,
    label=f"átlagsebesség = {average_speed:.1f} m/s"
)

axes[1].legend()

# Eredmények kiírása az ábrára
result_text = (
    f"Megtett út: s = {total_distance} m\n"
    f"Teljes idő: t = {total_time} t\n"
    f"Átlagsebesség: vátl = s / t = {average_speed:.1f} m/s\n"
    f"Elmozdulás: Δx = {displacement} m\n"
    f"Átlagos elmozdulási sebesség: Δx / t = {average_velocity:.1f} m/s"
)

fig.text(
    0.5,
    0.01,
    result_text,
    ha="center",
    va="bottom",
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black")
)

plt.tight_layout(rect=[0, 0.16, 1, 1])

# Mentés képként
plt.savefig("atlagsebesseg_grafikon.png", dpi=300)

# Megjelenítés
plt.show()