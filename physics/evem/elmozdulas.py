import matplotlib.pyplot as plt

# Mozgás adatai
x_start = 0
x_turn = 5
x_end = 0

# Fizikai mennyiségek
distance = abs(x_turn - x_start) + abs(x_end - x_turn)
displacement = x_end - x_start

# Ábra létrehozása
fig, ax = plt.subplots(figsize=(10, 4))

# Koordinátatengely
ax.axhline(0, linewidth=1)
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 1)

# Mozgás oda: 0 -> +5
ax.annotate(
    "",
    xy=(x_turn, 0.25),
    xytext=(x_start, 0.25),
    arrowprops=dict(arrowstyle="->", linewidth=2)
)

# Mozgás vissza: +5 -> 0
ax.annotate(
    "",
    xy=(x_end, -0.25),
    xytext=(x_turn, -0.25),
    arrowprops=dict(arrowstyle="->", linewidth=2)
)

# Pontok jelölése
ax.plot(x_start, 0, "o", markersize=8)
ax.plot(x_turn, 0, "o", markersize=8)

# Feliratok
ax.text(x_start, 0.1, "Origó\nx = 0 m", ha="center", va="bottom", fontsize=11)
ax.text(x_turn, 0.1, "Fordulópont\nx = +5 m", ha="center", va="bottom", fontsize=11)

ax.text(2.5, 0.45, "odaút: 5 m", ha="center", fontsize=12)
ax.text(2.5, -0.55, "visszaút: 5 m", ha="center", fontsize=12)

# Eredménydoboz
result_text = (
    f"Megtett út: s = 5 m + 5 m = {distance} m\n"
    f"Elmozdulás: Δx = x₂ - x₁ = 0 m - 0 m = {displacement} m"
)

ax.text(
    2.5,
    0.85,
    result_text,
    ha="center",
    va="center",
    fontsize=12,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black")
)

# Tengely beállítások
ax.set_xlabel("Helyzet az x tengelyen [m]", fontsize=12)
ax.set_yticks([])
ax.set_xticks(range(0, 6))
ax.set_title("Megtett út és elmozdulás oda-vissza mozgás esetén", fontsize=14)

plt.tight_layout()

# Mentés fájlba
plt.savefig("ut_es_elmozdulas.png", dpi=300)

# Megjelenítés
plt.show()