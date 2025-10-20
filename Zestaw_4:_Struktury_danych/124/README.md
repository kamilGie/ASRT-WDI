<picture>
  <source srcset="../../srt/zbior_zadan/124.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_124.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_124.png" alt="zadanie 124">
</picture>

```python
from math import inf

def Zadanie_124(Struktura):
    # Obliczanie najbliższego punktu od osi współrzędnych
    najblizszy_osi = inf
    for x, y in Struktura:
        odleglosc = max(abs(x), abs(y))  # Maksymalna odległość od osi dla tego punktu
        if  odleglosc < najblizszy_osi:
            najblizszy_osi = odleglosc

    # Jeśli najbliższy punkt do osi to (0, 0), zwracamy False
    if najblizszy_osi == 0:
        return False

    # Sprawdzanie obecności czterech wymaganych punktów w strukturze
    prawa_gora = (najblizszy_osi, najblizszy_osi)
    prawa_dol = (najblizszy_osi, -najblizszy_osi)
    lewa_gora = (-najblizszy_osi, najblizszy_osi)
    lewa_dol = (-najblizszy_osi, -najblizszy_osi)

    # Sprawdzamy, czy wszystkie punkty są obecne w strukturze
    return ( prawa_gora in Struktura and prawa_dol in Struktura and lewa_gora in Struktura and lewa_dol in Struktura)
```
# Opis Rozwiązania
Jeśli kwadrat istnieje i nie zawiera punktów w środku, jego wierzchołki będą znajdować się w odległości od osi współrzędnych równej odległości najbliższego punktu.

<div align="center">
  <video src="https://github.com/user-attachments/assets/f9bb3ca3-144a-439a-b598-b19baac992f7" width="400" />
</div>
    
Program wizualizacji znajduje się w rozwiązaniach. Klawisz `spacja` resetuje kwadrat, a klawisz `r` resetuje punkty.


---
Twoja gwiazdka pomaga w rozwoju repozytorium 👍
