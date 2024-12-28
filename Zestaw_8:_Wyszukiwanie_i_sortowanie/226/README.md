<picture>
  <source srcset="../../srt/zbior_zadan/226.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_226.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_226.png" alt="zadanie 226">
</picture>

```python
def Zadanie_226(T):
    """Istnieją 3 różne klocki: (1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4). Reszta to ich modyfikacje."""
    i, end = 0, len(T) - 1
    while i <= end:  # Przenoszę opcję 1 na początek, opcję 2 na koniec, a opcję 3 zostawiam na miejscu
        for j in range(4): # szukam indekus koloru 2
            if T[i][j] ==2:
                prev, next = T[i][(j - 1) % 4], T[i][(j + 1) % 4]  # Sąsiedzi koloru 2
                if {prev, next} == {1, 3}:  # Opcja 1: Na początek
                    T.insert(0, T.pop(i))
                    i += 1
                elif {prev, next} == {3, 4}:  # Opcja 3: Na koniec
                    T.append(T.pop(i))
                    end -= 1
                else:  # Opcja 2: Zostawiamy na miejscu
                    i += 1
                break
```