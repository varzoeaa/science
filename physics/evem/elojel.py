import numpy as np
import matplotlib.pyplot as plt

# Egyenes vonalú mozgás: előjel szemléltetése
# A negatív sebesség azt jelenti, hogy a test az x tengely
# negatív irányába mozog (visszafelé halad)

# Mozgás paraméterei
x0 = 10  # kezdő hely [m]
v = -3   # sebesség [m/s] – negatív: az origó felé tart

# Időintervallum: 0-tól 5 másodpercig, 100 lépésben
t = np.linspace(0, 5, 100)

# Helyzetfüggvény: x(t) = x0 + v*t = 10 - 3t
x = x0 + v * t

# Ábra létrehozása
plt.figure(figsize=(8, 5))
plt.plot(t, x, label=r"$x(t) = 10 - 3t$")

# Tengelyeken átmenő referenciaegyenesek
plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # x = 0 vonal
plt.axvline(0, color='gray', linestyle='--', linewidth=1)  # t = 0 vonal

plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('Mozgás grafikonja: x(t) = 10 - 3t')
plt.legend()
plt.grid(True)
plt.show()
