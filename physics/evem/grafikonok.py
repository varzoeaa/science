import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# =========================
# BEÁLLÍTÁSOK
# =========================

output_dir = Path("egyenes_vonalu_egyenletes_mozgas_grafikonok")
output_dir.mkdir(exist_ok=True)

# Mozgás adatai
x0 = 0          # kezdőhely [m]
v = 2           # állandó sebesség [m/s]
t_max = 10      # vizsgált idő [s]

# Időtengely
t = np.linspace(0, t_max, 300)

# Függvények
x = x0 + v * t          # hely-idő függvény
dx = x - x0             # elmozdulás
s = np.abs(v) * t       # megtett út
velocity = np.full_like(t, v)
acceleration = np.zeros_like(t)


# =========================
# SEGÉDFÜGGVÉNYEK
# =========================

def setup_axes(title, xlabel, ylabel):
    plt.figure(figsize=(8, 5))
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def save_plot(filename):
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=200)
    plt.close()


# =========================
# 1. HELY–IDŐ GRAFIKON
# =========================

setup_axes(
    "Hely–idő grafikon egyenes vonalú egyenletes mozgásnál",
    "idő, t [s]",
    "hely, x [m]"
)

plt.plot(t, x, linewidth=2, label=r"$x(t)=x_0+v\cdot t$")
plt.scatter([0], [x0], zorder=5, label=fr"Kezdőhely: $x_0={x0}$ m")
plt.legend()

save_plot("01_hely_ido_grafikon.png")


# =========================
# 2. ELMOZDULÁS–IDŐ GRAFIKON
# =========================

setup_axes(
    "Elmozdulás–idő grafikon",
    "idő, t [s]",
    "elmozdulás, Δx [m]"
)

plt.plot(t, dx, linewidth=2, label=r"$\Delta x = v\cdot t$")
plt.legend()

save_plot("02_elmozdulas_ido_grafikon.png")


# =========================
# 3. ÚT–IDŐ GRAFIKON
# =========================

setup_axes(
    "Megtett út–idő grafikon",
    "idő, t [s]",
    "megtett út, s [m]"
)

plt.plot(t, s, linewidth=2, label=r"$s=|v|\cdot t$")
plt.legend()

save_plot("03_ut_ido_grafikon.png")


# =========================
# 4. SEBESSÉG–IDŐ GRAFIKON
# =========================

setup_axes(
    "Sebesség–idő grafikon egyenletes mozgásnál",
    "idő, t [s]",
    "sebesség, v [m/s]"
)

plt.plot(t, velocity, linewidth=2, label=fr"$v={v}$ m/s")
plt.fill_between(t, 0, velocity, alpha=0.2, label="A görbe alatti terület = elmozdulás")
plt.legend()

save_plot("04_sebesseg_ido_grafikon.png")


# =========================
# 5. GYORSULÁS–IDŐ GRAFIKON
# =========================

setup_axes(
    "Gyorsulás–idő grafikon egyenletes mozgásnál",
    "idő, t [s]",
    "gyorsulás, a [m/s²]"
)

plt.plot(t, acceleration, linewidth=2, label=r"$a=0$")
plt.legend()

save_plot("05_gyorsulas_ido_grafikon.png")


# =========================
# 6. PÁLYA KOORDINÁTARENDSZERBEN
# =========================

setup_axes(
    "A test pályája az x tengelyen",
    "hely, x [m]",
    "y [m]"
)

x_path = x
y_path = np.zeros_like(x_path)

plt.plot(x_path, y_path, linewidth=2, label="A test pályája")
plt.scatter([x0], [0], zorder=5, label="Indulási pont")
plt.scatter([x[-1]], [0], zorder=5, label="Végpont")

for i in range(0, len(x_path), 40):
    plt.arrow(
        x_path[i],
        0,
        v * 0.2,
        0,
        head_width=0.15,
        head_length=0.25,
        length_includes_head=True
    )

plt.ylim(-1, 1)
plt.legend()

save_plot("06_palya_koordinatarendszerben.png")


# =========================
# 7. KÉPLET ÖSSZEFOGLALÓ ÁBRA
# =========================

plt.figure(figsize=(8, 5))
plt.axis("off")

text = (
    "Egyenes vonalú egyenletes mozgás\n\n"
    r"Hely-idő függvény:  $x(t)=x_0+v\cdot t$" "\n\n"
    r"Elmozdulás:  $\Delta x=x-x_0=v\cdot t$" "\n\n"
    r"Megtett út:  $s=|v|\cdot t$" "\n\n"
    r"Sebesség:  $v=\frac{\Delta x}{\Delta t}$ = állandó" "\n\n"
    r"Gyorsulás:  $a=0$"
)

plt.text(
    0.05,
    0.9,
    text,
    fontsize=16,
    va="top"
)

save_plot("07_keplet_osszefoglalo.png")


print(f"Kész! A PNG fájlok ide kerültek: {output_dir.resolve()}")